# Generated by Django 3.1.1 on 2021-04-13 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_test_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='test_code',
        ),
    ]
