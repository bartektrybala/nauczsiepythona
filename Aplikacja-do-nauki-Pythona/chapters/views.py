from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Chapter, Topic, UserApproach, Code
from users.models import Profile

from .forms import ApproachForm, UserCode
from .functions import exec_user_input

import operator


# Funkcja do "Kontunuuj naaukę"
def last_topic(approaches):
    last_approach = approaches[-1]
    last_topic_id = last_approach.topic.id
    return last_topic_id


def index(request):
    u = User.objects.all()
    users = sorted(u, key=operator.attrgetter('profile.points'), reverse=True)
    if request.user.is_authenticated:
        approaches = UserApproach.objects.filter(user=request.user)
        approaches = sorted(approaches, key=operator.attrgetter('topic.id'))
        if len(approaches) > 0:
            last_topic_id = last_topic(approaches)
        else:
            last_topic_id = 1
    else:
        last_topic_id = 1
    context = {'users': users, 'last_topic_id': last_topic_id}
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
    chapter = get_object_or_404(Chapter, id=chapter_id)
    topics = chapter.topic_set.all()
    context = {'chapter': chapter, 'topics': topics}
    return render(request, 'chapters/topic.html', context)


@login_required
def approach(request, topic_id):
    """Add a new approach for topic"""
    topic = Topic.objects.get(id=topic_id)

    approach, _ = UserApproach.objects.get_or_create(user=request.user, topic=topic)
    res = exec_user_input(approach.user_approach)

    if request.method != 'POST':
        if approach.user_approach:
            form = ApproachForm(instance=approach)
        else:
            approach.user_approach = topic.approach
            form = ApproachForm(instance=approach)
    else:
        form = ApproachForm(instance=approach, data=request.POST)
        points_f = Profile.objects.get(user=request.user)
        if form.is_valid():
            form.save()
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
                        approach.save()

                return HttpResponseRedirect(reverse('chapters:approach', args=[topic.id]))
    context = {'topic': topic, 'form': form, 'res': res, 'approach': approach}
    return render(request, 'chapters/approach.html', context)


def literatura(request):
    """Information about books."""
    return render(request, 'chapters/literatura.html')

@login_required
def pomoc(request):
    """Information about books."""
    chapters = Chapter.objects.order_by('id')
    context = {'chapters': chapters}
    return render(request, 'chapters/pomoc_list.html', context)


@login_required
def pomoc_chapter(request, chapter_id):
    """
        Auxliary info for every chapter.
    """
    chapter = get_object_or_404(Chapter, id=chapter_id)
    context = {
        "chapter": chapter
        }
    return render(request, 'chapters/pomoc.html', context)


@login_required
def kodowanie(request):
    """Code mirror for user"""
    code, _ = Code.objects.get_or_create(user=request.user)
    res = exec_user_input(code.test_code)

    if request.method != 'POST':
        form = UserCode(instance=code)
    else:
        form = UserCode(instance=code, data=request.POST)
        code_input = request.POST['test_code']
        res = exec_user_input(code_input)
        if form.is_valid():
            new_code = form.save(commit=False)
            new_code.user = request.user
            new_code.save()
            return HttpResponseRedirect(reverse('chapters:kodowanie'))

    context = {'form': form, 'res': res}
    return render(request, 'chapters/kodowanie.html', context)

