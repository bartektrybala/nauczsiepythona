# Generated by Django 3.1.7 on 2021-03-27 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0011_userapproach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapproach',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapters.topic'),
        ),
    ]