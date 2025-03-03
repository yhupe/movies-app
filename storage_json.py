from istorage import IStorage
import json
import os


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as fileobj:
                json.dump({}, fileobj)

    def list_movies(self):
        """ Lists all movies in the instantiated database."""

        with open(self.file_path, "r") as fileobj:
            data = json.loads(fileobj.read())

            return data

    def add_movie(self, title, year, rating, poster):
        """ Adds a movie and its information to the database"""

        with open(self.file_path, "r") as fileobj:
            data = json.loads(fileobj.read())

        data[title] = {
            "Rating": rating,
            "Year": year,
            "Poster": poster
        }

        json_str = json.dumps(data)

        with open(self.file_path, "w") as fileobj:
            fileobj.write(json_str)


    def delete_movie(self, title):
        """ Deletes a movie from the database"""

        with open(self.file_path, "r") as fileobj:
            data = json.loads(fileobj.read())

        list_of_all_data = data.copy()

        movie_index_to_be_removed = None

        for index, movie in enumerate(list_of_all_data):
            if movie["Film name"] == title:
                movie_index_to_be_removed = index

        list_of_all_data.pop(movie_index_to_be_removed)

        json_str = json.dumps(list_of_all_data)

        with open(self.file_path, "w") as fileobj:
            fileobj.write(json_str)

    def update_movie(self, title, rating):
        """ Updates the ranking of a movie"""

        with open(self.file_path, "r") as fileobj:
            data = json.loads(fileobj.read())

        list_of_all_data = data.copy()

        for index, movie in enumerate(list_of_all_data):
            if movie["Film name"] == title:
                movie_index_to_be_updated = index

                list_of_all_data[movie_index_to_be_updated]["Film name"] = title
                list_of_all_data[movie_index_to_be_updated]["Rating"] = rating

        json_str = json.dumps(list_of_all_data)

        with open(self.file_path, "w") as fileobj:
            fileobj.write(json_str)