class Movies:
    def __init__(self, title, premiere_date, genre, views):
        self.title = title
        self.premiere_date = premiere_date
        self.genre = genre
        self.views = views
        
    def __str__(self):
        return f'{self.title} {self.premiere_date}'

    def play(self, step=1):
        self.views += step


class TvSeries(Movies):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} S{self.season_number:.2f}E{self.episode_number:.2f}'

    def play(self, step=1):
        self.views += step