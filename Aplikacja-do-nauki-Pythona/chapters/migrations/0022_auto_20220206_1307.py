# Generated by Django 3.1.1 on 2022-02-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0021_chapter_code_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='code_text',
        ),
        migrations.AddField(
            model_name='topic',
            name='code_text',
            field=models.TextField(default=''),
        ),
    ]