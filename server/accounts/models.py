from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre, Movie

# # Create your models here.

class Profile(models.Model):
    title = models.CharField(max_length=10)
    image = models.CharField(max_length=100)
    
class User(AbstractUser):
    goal_of_month = models.IntegerField(default=1)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    favorite_genre = models.ManyToManyField(Genre, related_name='user_genre')
    is_superuser = models.BooleanField(default=False)
    save_movies = models.ManyToManyField(Movie, related_name="save_users",blank=True)
    profile_pic = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile',blank=True, null=True,default=1)