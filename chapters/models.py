from django.db import models


class Chapter(models.Model):
    """Chapters the user is learning about"""
    name = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Topic(models.Model):
    """Topic included in Chapters"""
    chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    text = models.TextField()
    approach = models.TextField(default='empty')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


