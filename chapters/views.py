from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


from .models import Chapter, Topic, UserApproach
from users.models import Profile

from .forms import ApproachForm
from .functions import exec_user_input

import operator


def index(request):
    u = User.objects.all()
    users = sorted(u, key=operator.attrgetter('profile.points'), reverse=True)
    context = {'users': users}
    return render(request, 'chapters/index.html', context)


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
    last_topic = Topic.objects.last()
    if topic_id == last_topic.id:
        next_topic_id = 1
    else:
        next_topic_id = topic_id+1
    try:
        approach = UserApproach.objects.get(user=request.user, topic=topic)
    except UserApproach.DoesNotExist:
        approach = UserApproach.objects.create(user=request.user, topic=topic)
    res = exec_user_input(approach.user_approach)

    if request.method != 'POST':
        if approach.points_awarded:
            form = ApproachForm(instance=approach)
        else:
            approach.user_approach = topic.approach
            form = ApproachForm(instance=approach)
    else:
        form = ApproachForm(instance=approach, data=request.POST)
        points_f = Profile.objects.get(user=request.user)

        user_input = request.POST['user_approach']
        res = exec_user_input(user_input)
        if type(res) == str:
            res_check = ''.join(res.split())
            topic_check = ''.join(topic.output.split())
            if form.is_valid():
                if res_check == topic_check:
                    messages.success(request, 'Correct!')
                    if not approach.points_awarded:
                        points_f.points += topic.points
                        approach.points_earned = topic.points
                        approach.points_awarded = True
                        points_f.save()
                        approach.points_earned = topic.points
                        approach.points_awarded = True

                form.save()
                return HttpResponseRedirect(reverse('chapters:approach', args=[topic.id]))
    context = {'topic': topic, 'topics': topics, 'form': form, 'res': res, 'approach': approach,
               'next_topic_id': next_topic_id}
    return render(request, 'chapters/approach.html', context)


def literatura(request):
    """Information about books."""
    return render(request, 'chapters/literatura.html')

