from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # goal_of_month = models.IntegerField(blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
