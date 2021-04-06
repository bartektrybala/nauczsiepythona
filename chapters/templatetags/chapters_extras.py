from django import template

register = template.Library()


@register.simple_tag
def get_chapter_points_tag(chapter, user):
    return chapter.user_chapter_points(user)


@register.simple_tag
def get_topic_points_tag(topic, user):
    return topic.user_topic_points(user)
