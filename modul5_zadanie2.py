from faker import Faker
fake = Faker()

import logging
logging.basicConfig(level=logging.INFO)

import random

from datetime import date

library = []
list_of_movies = []
list_of_series = []
date = date.today()

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

    def generate_views_x(self, x):
        for i in range(x):
            generate_views()

    #metoda dodająca wygenerowany tytuł do biblioteki filmów/seriali
    def add_to_library(self):
        library.append(self)

class TvSeries(Movies):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} S{self.season_number}E{self.episode_number}'

    def __eq__(self, other):
        return (
            self.title == other.title and
            self.premiere_date == other.premiere_date and
            self.genre == other.genre and
            self.views == other.views and
            self.episode_number == other.episode_number and
            self.season_number == other.season_number
            )

def sort_movies_series(elem, list_1, list_2):
    is_series = isinstance(elem, TvSeries)
    if is_series == False:
        list_1.append([elem.title, elem.premiere_date, elem.genre, elem.views])
    else:
        list_2.append([elem.title, elem.premiere_date, elem.genre, elem.views, elem.episode_number, elem.season_number])
    
def get_movies():
    for elem in library:
        sort_movies_series(elem, list_of_movies, list_of_series)
    list_of_movies.sort(key=lambda x: x[0])
    print(list_of_movies)


def get_series():
    for elem in library:
        sort_movies_series(elem, list_of_movies, list_of_series)
    list_of_series.sort(key=lambda x: x[0])
    print(list_of_series)

def search(title):
    for elem in library:
        if title.lower()==elem.title.lower():
            print(elem.title, elem.premiere_date, elem.genre, elem.views)

def generate_views():
    random_item = random.choice(library)
    random_number = random.randrange(1, 100)
    for i in range(random_number):
        random_item.play()

def top_titles(content_type):    
    list_1 = []
    list_2 = []

    if content_type.lower() == 'movie':

        for elem in library:
            sort_movies_series(elem, list_1, list_2)

        list_1.sort(key=lambda x:x[3], reverse=True)
        print(f'{list_1[0]}\n{list_1[1]}\n{list_1[2]}')

    if content_type.lower() == 'series':

        for elem in library:
            sort_movies_series(elem, list_1, list_2)

        list_2.sort(key=lambda x:x[3], reverse=True)
        print(f'{list_2[0]}\n{list_2[1]}\n{list_2[2]}')



if __name__ == "__main__":


    print('Biblioteka filmów i seriali')
    random_movie = Movies(title='Interstellar', premiere_date='07.11.2014', genre='Science Fiction', views=0)
    random_movie_2 = Movies(title='A Long Way Down', premiere_date='21.03.2014', genre='Black Comedy', views=0)
    random_movie_3 = Movies(title='Top Gun', premiere_date='12.05.1986', genre='Action', views = 0)
    random_series = TvSeries(title='Family Guy', premiere_date='31.01.1999', genre='Comedy', views=0, episode_number='01', season_number='01')
    random_series_2 = TvSeries(title='The Simpsons', premiere_date='17.12.1989', genre='Comedy', views=0, episode_number='01', season_number='01')
    random_series_3 = TvSeries(title='Black Mirror', premiere_date='04.12.2011', genre='Science Fiction', views=0, episode_number='01', season_number='01')

    random_movie.add_to_library()
    random_movie_2.add_to_library()
    random_movie_3.add_to_library()
    random_series.add_to_library()
    random_series_2.add_to_library()
    random_series_3.add_to_library()

    random_series.generate_views_x(1111)

    print(f'Najpopularniejsze filmy i seriale {date} \nFilmy:')

    top_titles('movie')

    print('Seriale:')

    top_titles('series')