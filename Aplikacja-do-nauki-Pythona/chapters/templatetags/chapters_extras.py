from django import template
from django.urls import reverse

from chapters.models import Topic

register = template.Library()


@register.simple_tag
def get_chapter_points_tag(chapter, user):
    return chapter.user_chapter_points(user)


@register.simple_tag
def get_topic_points_tag(topic, user):
    return topic.user_topic_points(user)


@register.simple_tag
def get_next_topic(topic_id):
    if topic_id == Topic.objects.last().id:
        topic_id = 1
    else:
        topic_id += 1
    return reverse('chapters:approach', args=[topic_id])

themes = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']
@register.simple_tag
def get_theme(counter):
    return themes[counter%8]

@register.simple_tag
def calc_chapter_progres(user, chapter):
    chapter_progres = chapter.user_chapter_points(user) / chapter.get_chapter_points() * 100
    return int(chapter_progres)
