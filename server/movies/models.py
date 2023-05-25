from django.db import models
from django.conf import settings
import requests

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)


class Movie(models.Model):
    movie_num = models.IntegerField()
    title = models.CharField(max_length=500)
    overview = models.TextField()
    poster_path = models.CharField(max_length=300)
    release_date= models.DateField(default=None,null=True, blank=True)
    popularity = models.IntegerField()
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    backdrop_path = models.CharField(max_length=300)
    # save_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='save_movies')

# def save_genre():
#     URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=3bf4d020baa9f161f8eaac60d2ab7205&language=ko-kr'
#     genres = requests.get(URL).json()

#     for genre_Data in genres['genres']:
#         genre = Genre(
#             name = genre_Data['name']
#         )
#         genre.save()
# save_genre()


# def save_movie():
#     for page in range(1,3):
#         URL = "https://api.themoviedb.org/3/movie/popular?api_key=3bf4d020baa9f161f8eaac60d2ab7205&language=ko-KR&page={page}"
        
#         response = requests.get(URL)
#         data = response.json()

#         for movie_data in data['results']:
#             movie = Movie(
#                 title = movie_data['title'],
#                 release_date= movie_data['release_date'],
#                 popularity= movie_data['popularity'],
#                 vote_average= movie_data['vote_average'],
#                 overview= movie_data['overview'],
#                 poster_path= movie_data['poster_path'],
                
#             )
           

#             # movie.genres.set(movie_data['genre_ids'])
#             # for genre_id in movie_data['genre_ids']:
#             #     genre = Genre.objects.get(pk=genre_id)
#             #     movie.genres.add(genre)
            
#             movie.save()
