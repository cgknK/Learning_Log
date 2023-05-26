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
]

"""
NOTE
There’s a subtle but important dif erence between topic.id and topic_id. The
expression topic.id examines a topic and retrieves the value of the corresponding
ID. The variable topic_id is a reference to that ID in the code. If you run into
errors when working with IDs, make sure you’re using these expressions in the
appropriate ways.
"""