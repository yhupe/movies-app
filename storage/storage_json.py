from storage.istorage import IStorage
import json
import os


class StorageJson(IStorage):
    """ Class inherits from class IStorage and handles listing, adding,
        deleting and updating movie information saved as .json file.
        """

    def __init__(self, file_path):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as fileobj:
                json.dump({}, fileobj)

    def list_movies(self):

        with open(self.file_path, "r") as fileobj:
            data = json.loads(fileobj.read())

        return data


    def add_movie(self, title, rating, year, poster):

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

        with open(self.file_path, "r") as fileobj:
            data = json.loads(fileobj.read())

            if title in data.keys():
                data.pop(title)

        json_str = json.dumps(data)

        with open(self.file_path, "w") as fileobj:
            fileobj.write(json_str)


    def update_movie(self, title, rating):

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