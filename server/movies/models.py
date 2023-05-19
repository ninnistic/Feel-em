from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=True)

class Movie(models.Model):
    
    title = models.CharField(max_length=500)
    overview = models.TextField()
    poster_path = models.CharField(max_length=300)
    release_date= models.DateField()
    popularity = models.IntegerField()
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    save_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='save_movies')