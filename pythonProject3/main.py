import json
import xml.etree.ElementTree as ET

# Класс для представления жанра кино
class Genre:
    def __init__(self, name):
        self.name = name

# Базовый класс для всех видов медиа (фильмы, сериалы и т. д.)
class Media:
    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director

# Класс для представления актеров
class Actor:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

# Класс для представления фильма
class Movie(Media):
    def __init__(self, title, year, director, genre, duration, actors):
        super().__init__(title, year, director)
        self.genre = genre
        self.duration = duration
        self.actors = actors

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "genre": self.genre.name,
            "duration": self.duration,
            "actors": [actor.name for actor in self.actors]
        }

# Класс для представления сериала
class TVShow(Media):
    def __init__(self, title, year, director, seasons, episodes_per_season):
        super().__init__(title, year, director)
        self.seasons = seasons
        self.episodes_per_season = episodes_per_season
        self.genre = Genre("action")  # Композиция - у сериала есть жанр

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "director": self.director,

            "seasons": self.seasons,
            "episodes_per_season": self.episodes_per_season,
            "genre": self.genre.name,
        }

# Создаем экземпляры классов
action_genre = Genre("Action")
comedy_genre = Genre("Comedy")

actor1 = Actor("Actor 1", 1980)
actor2 = Actor("Actor 2", 1990)

movie = Movie("Movie 1", 2022, "Director 1", action_genre, 120, [actor1, actor2])
tv_show = TVShow("TV Show 1", 2023, "Director 2", 5, 10)

# Сохраняем данные в формате JSON
movie_data = movie.to_dict()
tv_show_data = tv_show.to_dict()

with open("movie.json", "w") as movie_file:
    json.dump(movie_data, movie_file, indent=4)

with open("tv_show.json", "w") as tv_show_file:
    json.dump(tv_show_data, tv_show_file, indent=4)

# Сохраняем данные в формате XML с использованием ElementTree
movie_root = ET.Element("Movie")
for key, value in movie_data.items():
    ET.SubElement(movie_root, key).text = str(value)

tv_show_root = ET.Element("TVShow")
for key, value in tv_show_data.items():
    ET.SubElement(tv_show_root, key).text = str(value)

movie_tree = ET.ElementTree(movie_root)
tv_show_tree = ET.ElementTree(tv_show_root)

movie_tree.write("movie.xml")
tv_show_tree.write("tv_show.xml")