from django.db import models
from django.contrib.auth.models import User


SKILL_LEVELS = (
    (0, 'Początkujący'),
    (10, 'Nowicjuesz'),
    (20, 'Zaawansowany Początkujący'),
    (40, 'Młodszy Programista'),
    (60, 'Średniozaawansowany Programista'),
    (80, 'Biegły Programista'),
    (100, 'Ekspert'),
    (130, 'Geniusz'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Ustawienia profilu"

    @property
    def skill_level(self):
        for level_points, level in reversed(SKILL_LEVELS):
            if self.points >= level_points:
                return level

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
            Set is_staff flag True for enable admin page for users.
        """
        if self.profile_image._file is None:
            self.profile_image = self._meta.get_field('profile_image').default
        if not self.pk:
            self.user.is_staff = True
            self.user.save()
        super().save()
