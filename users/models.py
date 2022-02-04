from django.db import models
from django.contrib.auth.models import User


EDUCATION_CHOICES = (
    ('1', 'Primary School'),
    ('2', 'High School'),
    ('3', 'University'),
    ('4', 'College'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.CharField(choices=EDUCATION_CHOICES, max_length=200)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def save(self):
        """
            Set is_staff flag True for enable admin page for users.
        """
        if not self.pk:
            self.user.is_staff = True
            self.user.save()
        super().save()
