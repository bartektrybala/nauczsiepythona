# Generated by Django 3.1.7 on 2021-03-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0002_topic_approach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='approach',
            field=models.TextField(default='empty'),
        ),
    ]
