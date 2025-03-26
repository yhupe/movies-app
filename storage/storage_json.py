from storage.istorage import IStorage
import json
import os


def read_json_data(file_path):
    """Function to support reading .json files,
    returns dictionary of dictionaries, if no file found under
    file path, empty dictionary is returned."""

    try:
        with open(file_path, "r") as fileobj:
            return json.loads(fileobj.read())
    except FileNotFoundError:
        return {}

def write_json_data(file_path, data):
    """Function so support writing .json files after CRUD actions made,
     to safe latest version of .json storage.
     Returns nothing. """

    json_str = json.dumps(data)
    with open(file_path, "w") as fileobj:
        fileobj.write(json_str)


class StorageJson(IStorage):
    """Class inherits from class IStorage and handles listing, adding,
        deleting and updating movie information saved as .json file.
        """

    def __init__(self, file_path):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as fileobj:
                json.dump({}, fileobj)

    def list_movies(self):
        """Class Method to fetch all existing movie records from
        .json file storage, returns a dict of dicts."""

        return read_json_data(self.file_path)

    def add_movie(self, title, rating, year, poster):
        """ Reads all existing movies, adds a new movie record as passed
        to the method and saves new movie record along with all records to .json file"""

        data = read_json_data(self.file_path)

        data[title] = {
            "Rating": rating,
            "Year": year,
            "Poster": poster
        }

        write_json_data(self.file_path, data)

    def delete_movie(self, title):
        """Reads all existing movies, deletes a movie record as passed
        to the method and saves remaining movie records .json file"""

        data = read_json_data(self.file_path)

        if title in data.keys():
            data.pop(title)

        write_json_data(self.file_path, data)

    def update_movie(self, title, rating):
        """Reads all existing movies, updates a movie record as passed
        to the method and saves updated movie record along with existing records to .json file"""

        data = read_json_data(self.file_path)

        list_of_all_data = data.copy()

        for index, movie in enumerate(list_of_all_data):
            if movie["Film name"] == title:
                movie_index_to_be_updated = index

                list_of_all_data[movie_index_to_be_updated]["Film name"] = title
                list_of_all_data[movie_index_to_be_updated]["Rating"] = rating

        write_json_data(self.file_path, data)