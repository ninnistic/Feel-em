from django.db import models
from movies.models import Movie
from django.conf import settings
# Create your models here.
class Mood(models.Model):
    title = models.CharField(max_length=10)
    image = models.CharField(max_length=100)
    
class Feelog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='feelogs')
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, related_name='mood_feelog')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_feelogs',blank=True)
