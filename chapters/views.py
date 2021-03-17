from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Chapter, Topic
from .forms import TopicForm


def index(request):
    """Home page for application"""
    return render(request, 'chapters/index.html')


def chapters(request):
    """Show all chapters"""
    chapters = Chapter.objects.order_by('id')
    context = {'chapters': chapters}
    return render(request, 'chapters/chapters.html', context)


def topic(request, chapter_id):
    """Show all topics of chapter"""
    chapter = Chapter.objects.get(id=chapter_id)
    topics = chapter.topic_set.all()
    context = {'chapter': chapter, 'topics': topics}
    return render(request, 'chapters/topic.html', context)


def approach(request, topic_id):
    """Add a new approach for topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('chapters:approach', args=[topic.id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'chapters/approach.html', context)

