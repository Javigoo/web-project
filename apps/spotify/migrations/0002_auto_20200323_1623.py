# Generated by Django 3.0.4 on 2020-03-23 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='refresh_token',
        ),
    ]
