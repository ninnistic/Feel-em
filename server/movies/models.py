from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=500)
    overview = models.TextField()
    poster_path = models.CharField(max_length=300)
    release_date= models.DateTimeField()
    popularity = models.IntegerField()
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='movies')
