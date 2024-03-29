"""Defines URL patterns for chapters."""


from django.urls import path


from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Literatura
    path('literatura/', views.literatura, name='literatura'),

    # Kodowanie
    path('kodowanie/', views.kodowanie, name='kodowanie'),

    # Pomoc
    path('pomoc/', views.pomoc, name='pomoc'),
    path('pomoc/<int:chapter_id>/', views.pomoc_chapter, name='pomoc_chapter'),

    # Show all chapters and topics
    path('chapters/', views.chapters, name='chapters'),
    path('chapters/<int:chapter_id>/', views.topic, name='topic'),

    # Approach for the topic
    path('topic/<int:topic_id>', views.approach, name='approach'),
]

