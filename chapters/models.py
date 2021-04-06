from django.db import models
from django.contrib.auth.models import User
from next_prev import next_in_order, prev_in_order


class Chapter(models.Model):
    """Chapters the user is learning about"""
    name = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

    def get_chapter_points(self):
        topics = Topic.objects.filter(chapter_id=self.id)
        ch_points = 0
        for topic in topics:
            ch_points += topic.points
        return ch_points

    def user_chapter_points(self, user):
        topics = Topic.objects.filter(chapter_id=self.id)
        user_points = 0
        for topic in topics:
            approaches = topic.userapproach_set.all()
            for approach in approaches:
                if approach.user == user:
                    user_points += approach.points_earned
        return user_points


class Topic(models.Model):
    """Topic included in Chapters"""
    chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    text = models.TextField()
    approach = models.TextField(default='print("Hello World!")')
    points = models.IntegerField(default=3)
    date_added = models.DateTimeField(auto_now_add=True)
    output = models.TextField(default='Hello World!')

    def __str__(self):
        return self.name

    def user_topic_points(self, user):
        approaches = self.userapproach_set.all()
        user_topic_points = 0
        for approach in approaches:
            if approach.user == user:
                user_topic_points = approach.points_earned
        return user_topic_points


class UserApproach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user_approach = models.TextField(default='')
    points_awarded = models.BooleanField(default=False)
    points_earned = models.IntegerField(default=0)
