from faker import Faker
fake = Faker()

import logging
logging.basicConfig(level=logging.INFO)

library = []

class Movies:
    def __init__(self, title, premiere_date, genre, views):
        self.title = title
        self.premiere_date = premiere_date
        self.genre = genre
        self.views = views
        
    def __str__(self):
        return f'{self.title} {self.premiere_date}'

    def __eq__(self, other):
        return (
            self.title == other.title and
            self.premiere_date == other.premiere_date and
            self.genre == other.genre and
            self.views == other.views
            )

    def play(self):
        self.views += 1

    #metoda dodająca wygenerowany tytuł do biblioteki filmów/seriali
    def add_to_library(self, value):
        #movie = []
        #movie.append(self.title)
        #movie.append(self.premiere_date)
        #movie.append(self.genre)
        #movie.append(self.views)
        library.append(value)

class TvSeries(Movies):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} S{self.season_number:.2f}E{self.episode_number:.2f}'

    def __eq__(self, other):
        return (
            self.title == other.title and
            self.premiere_date == other.premiere_date and
            self.genre == other.genre and
            self.views == other.views and
            self.episode_number == other.episode_number and
            self.season_number == other.season_number
            )

    def play(self):
        self.views += 1

    #metoda dodająca wygenerowany tytuł do biblioteki filmów/seriali
    def add_to_library(self, value):
        movie = []
        movie.append(self.title)
        movie.append(self.premiere_date)
        movie.append(self.genre)
        movie.append(self.views)
        movie.append(self.episode_number)
        movie.append(self.season_number)
        library.append(movie)


def get_movies(value):
    only_movies = []
    for elem in value:
        if elem == Movies:
            only_movies.append(elem)
    only_movies.sort(key=lambda movies: movies.self.title)
    print(only_movies)
    

random_movie = Movies(title='Interstellar', premiere_date='07.11.2014', genre='Science Fiction', views=0)
random_tv_series = TvSeries(title='Family Guy', premiere_date='31.01.1999', genre='Comedy', views=0, episode_number=1, season_number=1)

random_movie.add_to_library(random_movie)
random_tv_series.add_to_library(random_tv_series)
print(library)

print(type(random_movie.title))

get_movies(library)

print(random_movie.views)

random_movie.play

print(random_movie.views)