from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Eğer login gibi hazır bir view func. @login_required decorator'ü ile 
#kısıtlamak istersek, nasıl yaparız?

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            # makemigrate ve migrate neden çalıştır mıyoruz? db'ye nereden
            #users kısımı açıldı ayarlandı?
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            #return redirect('') buda anasayfa değil mi?
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)