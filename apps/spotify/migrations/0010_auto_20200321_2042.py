# Generated by Django 3.0.4 on 2020-03-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0009_auto_20200321_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='song',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(to='spotify.Song'),
        ),
    ]