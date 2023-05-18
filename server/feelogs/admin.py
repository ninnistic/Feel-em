from django.contrib import admin
from movies.models import Movie, Genre
from feelogs.models import Feelog, Mood
# Register your models here.
admin.site.register(Movie)
admin.site.register(Feelog)
admin.site.register(Mood)
admin.site.register(Genre)
