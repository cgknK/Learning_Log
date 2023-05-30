from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for Learning Log."""
    # 'learning_logs/index.html' bu url patterni neden learning_logs ile başlıyor?
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    # store the resulting queryset in topics.
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    # Detail page for a single topic.
    #topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    _check_topic_owner(topic.owner, request.user)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # conmmit=False araştır.
            new_topic = form.save(commit=False)
            #new_topic = form.save()
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    # An invalid form will include some default error messages to help the user 
    #submit acceptable data. _Hani nerede?
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    _check_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    _check_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        #ne demek initial request?
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            # Buradaki girdi nasıl halihazırda doğru konuyla ilişkili?
            form.save()
            # Burada neden new_entry'deki gibi topic_id=topic_id değil?
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

# Bir class içerinde olmamasına rağmen helper method yerine helper fonksiyon
#tanımlanabiliyor mu? Cevap evet ise aşağıdaki kullanım doğrumu ?
# Bu kullanımın söyle bir yetersizliği var; eğer henüz oluşturulmamış-db'de 
#yer almayan birşeyi çağırırsak Http404 yerine bulunmadığına-var olmadığına- 
#dair bir hata dönderiliyor. Buna önlem al.
def _check_topic_owner(topic_owner, request_user):
    """
    We make sure the user associated with a topic matches the currently 
    logged in user.
    """
    # Make sure the topic belongs to the current user.
    if topic_owner != request_user:
        # direkt return demekle tam olarak ne farkı var?
        # raise ne? Kendi içinde mi return'ü var topic()'in
        # if dışına veya else bir return yada başka bir raise eklemek bu durum 
        #için mantıklı mı?
        raise Http404