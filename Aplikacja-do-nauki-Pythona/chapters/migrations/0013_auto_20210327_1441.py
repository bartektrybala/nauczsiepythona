# Generated by Django 3.1.7 on 2021-03-27 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chapters', '0012_auto_20210327_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapproach',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
