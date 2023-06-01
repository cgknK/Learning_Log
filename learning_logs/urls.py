"""Burada herhangi bir çalışan fonksiyon olmamasına rağmen urlpatterns nasıl
eşleşen url'i views.py'ye gönderiyor. Bu alien_invasion'daki settings.py gibi
çalışmıyor mu?"""
"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    # views.index() olması gerekmiyor mu index() bir fonksiyon çünkü.
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # Page for adding a new topic
    # İyi de her kullanıcı için aynı url olmuyor mu? Bu anlamsız bir çakışma 
    #durumu değil mi?(new_topic/<int:user_id> gibi olması gerekmiyor mu?)
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

"""
NOTE
There’s a subtle but important dif erence between topic.id and topic_id. The
expression topic.id examines a topic and retrieves the value of the corresponding
ID. The variable topic_id is a reference to that ID in the code. If you run into
errors when working with IDs, make sure you’re using these expressions in the
appropriate ways.
"""