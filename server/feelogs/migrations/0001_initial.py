# Generated by Django 3.2.18 on 2023-05-18 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feelog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('like_users', models.ManyToManyField(related_name='like_feelogs', to=settings.AUTH_USER_MODEL)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mood_feelog', to='feelogs.mood')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feelogs', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
