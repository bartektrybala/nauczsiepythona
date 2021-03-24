from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Chapter, Topic
from .forms import TopicForm
from .functions import exec_user_input

import sys

def index(request):
    """Home page for application"""
    return render(request, 'chapters/index.html')


@login_required
def chapters(request):
    """Show all chapters"""
    chapters = Chapter.objects.order_by('id')
    context = {'chapters': chapters}
    return render(request, 'chapters/chapters.html', context)


@login_required
def topic(request, chapter_id):
    """Show all topics of chapter"""
    chapter = Chapter.objects.get(id=chapter_id)
    topics = chapter.topic_set.all()
    context = {'chapter': chapter, 'topics': topics}
    return render(request, 'chapters/topic.html', context)


@login_required
def approach(request, topic_id):
    """Add a new approach for topic"""
    topic = Topic.objects.get(id=topic_id)
    chapter = topic.chapter
    topics = chapter.topic_set.all()
    res = exec_user_input(topic.approach)
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        user_input = request.POST['approach']
        res = exec_user_input(user_input)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('chapters:approach', args=[topic.id]))

    context = {'topic': topic, 'topics': topics, 'form': form, 'res': res}
    return render(request, 'chapters/approach.html', context)


def literatura(request):
    """Information about books."""
    return render(request, 'chapters/literatura.html')

