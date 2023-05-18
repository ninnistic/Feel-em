# Generated by Django 3.2.1 on 2023-05-18 17:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=300)),
                ('release_date', models.DateField()),
                ('popularity', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('save_users', models.ManyToManyField(related_name='save_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
