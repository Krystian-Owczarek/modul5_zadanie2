class Movies:
    def __init__(self, title, premiere_date, genre, views):
        self.title = title
        self.premiere_date = premiere_date
        self.genre = genre
        self.views = views


class TvSeries(Movies):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number