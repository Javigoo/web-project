# Generated by Django 3.0.4 on 2020-03-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0005_spotify_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='song',
        ),
        migrations.AddField(
            model_name='artist',
            name='songs',
            field=models.ManyToManyField(related_name='Artist', to='spotify.Song'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
