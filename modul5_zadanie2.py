from faker import Faker
fake = Faker()

import logging
logging.basicConfig(level=logging.INFO)

import random

library = []
list_of_movies = []
list_of_series = []

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

    def play(self):
        self.views += 1

    #metoda dodająca wygenerowany tytuł do biblioteki filmów/seriali
    def add_to_library(self):
            library.append(self)
    
def get_movies():
    for elem in library:
        is_series = isinstance(elem, TvSeries)
        if is_series == False:
            list_of_movies.append([elem.title, elem.premiere_date, elem.genre, elem.views])
    list_of_movies.sort(key=lambda x: x[0])
    print(list_of_movies)


def get_series():
    for elem in library:
        is_series = isinstance(elem, TvSeries)
        if is_series == True:
            list_of_series.append([elem.title, elem.premiere_date, elem.genre, elem.views])
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

def generate_views_x_10():
    for i in range(10):
        generate_views()

def top_titles(content_type):    


    if content_type.lower() == 'movie':
        list_1 = []

        for elem in library:
            is_series = isinstance(elem, TvSeries)
            if is_series == False:
                list_1.append(elem)

        for i in range(3):

            movie = list_1[0]

            for number in list_1:
                if number.views > movie.views:
                    movie = number
            print(f'top watched is {movie.title} with {movie.views} views')
            


    if content_type.lower() == 'tv series':
        list_2 = []

        for elem in library:
            is_series = isinstance(elem, TvSeries)
            if is_series == True:
                list_2.append(elem)

        for i in range(15):

            tv_series = list_2[0]

            for number in list_2:
                if number.views > tv_series.views:
                    tv_series = number
            print(f'top watched is {tv_series.title} with {tv_series.views} views')
            



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

generate_views_x_10()

print(random_movie.views)
print(random_movie_2.views)
print(random_movie_3.views)
print(random_series.views)
print(random_series_2.views)
print(random_series_3.views)

top_titles('tv series')

'''
if __name__ == "__main__":

    print('Biblioteka filmów i seriali')
    random_movie = Movies(title='Interstellar', premiere_date='07.11.2014', genre='Science Fiction', views=0)
    random_movie_2 = Movies(title='A Long Way Down', premiere_date='21.03.2014', genre='Black Comedy', views=0)
    random_movie_3 = Movies(title='Top Gun', premiere_date='12.05.1986', genre='Action', views = 0)
    random_series = TvSeries(title='Family Guy', premiere_date='31.01.1999', genre='Comedy', views=0, episode_number='01', season_number='01')
    random_series_2 = TvSeries(title='The Simpsons', premiere_date='17.12.1989', genre='Comedy', views=0, episode_number='01', season_number='01')
    random_series_3 = TvSeries(title='Black Mirror', premiere_date='04.12.2011', genre='Science Fiction', views=0, episode_number='01', season_number='01')

    generate_views_x_10()

    print('Najpopularniejsze filmy i seriale {datetime.now()}')

'''