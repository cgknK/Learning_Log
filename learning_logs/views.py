from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for Learning Log."""
    # 'learning_logs/index.html' bu url patterni neden learning_logs ile başlıyor?
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    # store the resulting queryset in topics.
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    # Detail page for a single topic.
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
