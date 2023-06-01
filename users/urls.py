"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    #Bu neden '' boş?
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    # Bunda neden views yazıyoruz, defaultu yok mu?
    # http://localhost:8000/users/register/ ile eşleşmesi için gerekli olan
    #users/ nereden geliyor?
    path('register/', views.register, name='register'),
]