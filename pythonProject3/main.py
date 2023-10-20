import json
import xml.etree.ElementTree as ET

class Media:
    def __init__(self, title, duration, author):
        self.title = title
        self.duration = duration
        self.author = author

    def to_dict(self):
        return {
            'title': self.title,
            'duration': self.duration,
            'author': self.author
        }


class Movie(Media):
    def __init__(self, title, duration, author, director, genre):
        super().__init__(title, duration, author)
        self.director = director
        self.genre = genre

    def to_dict(self):
        movie_data = super().to_dict()
        movie_data.update({
            'title': self.title,
            'duration': self.duration,
            'author': self.author,
            'director': self.director,
            'genre': self.genre
        })
        return movie_data


class TVShow(Media):
    def __init__(self, title, duration, author, season, episode):
        super().__init__(title, duration, author)
        self.season = season
        self.episode = episode

    def to_dict(self):
        tvshow_data = super().to_dict()
        tvshow_data.update({
            'title': self.title,
            'duration': self.duration,
            'author': self.author,
            'season': self.season,
            'episode': self.episode
        })
        return tvshow_data

# Создаем несколько объектов
movie1 = Movie("movie 1", 150, "Autor 1", "Director 1", "Comedy")
movie2 = Movie("Movie 2", 150, "Autor 2", "Director 2", "Comedy")
tvshow1 = TVShow("TV Show 1", 30, "Autor 1", 1, 3)
tvshow2 = TVShow("TV Show 2", 30, "Season 1", 2, 3)

# Преобразуем объекты в словари
data = {
    'movies': [movie1.to_dict(), movie2.to_dict()],
    'tvshows': [tvshow1.to_dict(), tvshow2.to_dict()]
}

# Сохраняем данные в формате JSON
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Создаем XML-структуру
root = ET.Element("media")
for movie in [movie1, movie2]:
    movie_element = ET.SubElement(root, "movie")
    for key, value in movie.to_dict().items():
        ET.SubElement(movie_element, key).text = str(value)

for tvshow in [tvshow1, tvshow2]:
    tvshow_element = ET.SubElement(root, "tvshow")
    for key, value in tvshow.to_dict().items():
        ET.SubElement(tvshow_element, key).text = str(value)

# Сохраняем данные в формате XML
tree = ET.ElementTree(root)
tree.write('data.xml')
with open('data_from_json.json', 'r') as json_file:
    loaded_data = json.load(json_file)
with open('data_to_json.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)
