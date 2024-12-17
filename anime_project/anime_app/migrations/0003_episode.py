# Generated by Django 5.1.4 on 2024-12-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0002_alter_comment_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_url', models.URLField()),
            ],
        ),
    ]
