import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feelem.settings')

import django
django.setup()

from movies.models import Genre, Movie
import requests


# 원래는 models.py 아래에 쓴대서 아래 코드들을 movies/models.py 아래에 저장하고 호출함. 
# 호출 안되면서 다양한 에러가 뜬다..! 그래서 폴더를 옮김
# feelem 모듈이 없다는 에러... 혹시 해당 코드 사용 가능하다면, 사용해보기
def save_genre():
    URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=3bf4d020baa9f161f8eaac60d2ab7205&language=ko-kr'
    genres = requests.get(URL).json()

    for genre_Data in genres['genres']:
        genre = Genre(
            name = genre_Data['name'],
            genre_ids = genre_Data['id']
        )
        genre.save()

def save_movie():
    for page in range(3,6):
        print(page)
        URL = f"https://api.themoviedb.org/3/movie/popular?api_key=3bf4d020baa9f161f8eaac60d2ab7205&language=ko-KR&page={page}"

        
        response = requests.get(URL)
        data = response.json()
        
        for movie_data in data['results']:
            movie = Movie(
                title = movie_data['title'],
                release_date= movie_data['release_date'],
                popularity= movie_data['popularity'],
                vote_average= movie_data['vote_average'],
                overview= movie_data['overview'],
                poster_path= movie_data['poster_path'],
               )
            movie.save()
            movie.genres.set(movie_data['genre_ids'])

        # movie.genres.set(movie_data['genre_ids'])
        # for genre_id in movie_data['genre_ids']:
        #     genre = Genre.objects.get(genre_ids=genre_id)
        #     print(genre)
        #     movie.genres.add(genre)
            
            

if __name__=='__main__':
    save_genre()
    save_movie()