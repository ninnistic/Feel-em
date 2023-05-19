from django.db import models
from django.contrib.auth.models import AbstractUser


# # Create your models here.
class User(AbstractUser):
    goal_of_month = models.IntegerField(default=1)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    is_superuser = models.BooleanField(default=False)