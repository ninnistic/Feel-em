import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feelem.settings')

import django

django.setup()

from movies.models import Genre, Movie
import requests

def save_genre():
    URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=3bf4d020baa9f161f8eaac60d2ab7205&language=ko-kr'
    genres = requests.get(URL).json()

    for genre_Data in genres['genres']:
        genre = Genre(
            name = genre_Data['name'],
            id = genre_Data['id'],
            )
        genre.save()

def save_movie():
    for page in range(1,20):
        print(page)
        URL = f"https://api.themoviedb.org/3/movie/popular?api_key=3bf4d020baa9f161f8eaac60d2ab7205&language=ko-KR&page={page}"

        
        response = requests.get(URL)
        data = response.json()
        
        for movie_data in data['results']:
            if 'release_date' not in movie_data:
                continue
            release_date = movie_data['release_date']

            if int(release_date[:4]) >= 2010:
                title = movie_data['title']
                adult = ['엄마','섹스','오르가즘','쾌락','막내 처제', '옥보단','슈퍼 마리오 브라더스','장화신은 고양이: 끝내주는 모험','피터팬 & 웬디','매기 심슨의 \"베이비 로그 원\"','매기','슬라임']
                if not any(word in title for word in adult):
                    if movie_data['overview']:
                        if movie_data['backdrop_path']:

                            movie = Movie.objects.create(
                                movie_num = movie_data['id'],
                                title = movie_data['title'],
                                release_date= movie_data['release_date'],
                                popularity= movie_data['popularity'],
                                vote_average= movie_data['vote_average'],
                                overview= movie_data['overview'],
                                poster_path= movie_data['poster_path'],
                                backdrop_path = movie_data['backdrop_path'],
                            )
                            genre_ids = movie_data['genre_ids']
                            genres = Genre.objects.filter(id__in = genre_ids)
                            
                            movie.genres.set(genres)

                            movie.save()

save_genre()
save_movie()