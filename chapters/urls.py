"""Defines URL patterns for chapters."""


from django.urls import path


from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Literatura
    path('literatura/', views.literatura, name='literatura'),

    # Kodowanie
    path('kodowanie', views.kodowanie, name='kodowanie'),

    # Show all chapters and topics
    path('chapters/', views.chapters, name='chapters'),
    path('chapters/<int:chapter_id>/', views.topic, name='topic'),

    # Approach for the topic
    path('topic/<int:topic_id>', views.approach, name='approach'),
]

