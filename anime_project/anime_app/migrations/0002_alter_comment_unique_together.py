# Generated by Django 5.1.4 on 2024-12-17 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('user_name', 'episode_id')},
        ),
    ]
