# Generated by Django 3.1.1 on 2021-04-13 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210413_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='kod',
            new_name='test_code',
        ),
    ]
