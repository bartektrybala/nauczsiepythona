# Generated by Django 3.1.7 on 2021-03-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0013_auto_20210327_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapproach',
            name='points_awarded',
            field=models.IntegerField(default=0),
        ),
    ]