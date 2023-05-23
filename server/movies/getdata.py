import requests
import json

def get_movies():
    all_movies = []

    for page in range(1, 5):
        URL = f"https://api.themoviedb.org/3/movie/popular?api_key=3bf4d020baa9f161f8eaac60d2ab7205&language=ko-KR&page={page}"
        movies = requests.get(URL).json()

        for movie in movies['results']:
            release_date = movie.get('release_date')
            if release_date and int(release_date[:4]) >= 2010:
                title = movie.get('title')
                adult = ['막내 처제', '옥보단']
                if not any(word in title for word in adult):
                    if movie.get('release_date', '') and movie.get('poster_path', ''):
                        fields = {
                            'movie_num': movie['id'],
                            'title': movie['title'],
                            'release_date': movie['release_date'],
                            'popularity': movie['popularity'],
                            'vote_average': movie['vote_average'],
                            'overview': movie['overview'],
                            'poster_path': movie['poster_path'],
                            'genres': movie['genre_ids']
                        }

                        data = {
                            "model": "movies.Movie",
                            "fields": fields,
                        }

                        all_movies.append(data)

    with open("movie.json", "w", encoding="utf-8") as make_json:
        json.dump(all_movies, make_json, indent="\t", ensure_ascii=False)

get_movies()

def get_genres():
    all_genres = []

    URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key=3bf4d020baa9f161f8eaac60d2ab7205&language=ko-kr'
    genres = requests.get(URL).json()

    for genre in genres['genres']:
        fields = {
            'name': genre['name']
        }

        data = {
            "pk": genre['id'],
            "model": "movies.Genre",
            "fields": fields,
        }

        all_genres.append(data)

    with open("genre.json", "w", encoding="utf-8") as w:
        json.dump(all_genres, w, indent="\t", ensure_ascii=False)

get_genres()
