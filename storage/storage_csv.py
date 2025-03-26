from storage.istorage import IStorage
import csv
import os


def read_csv_data(file_path):
    """Function to support reading .csv files,
    returns dictionary of dictionaries, if no file found under
    file path, empty dictionary is returned."""

    try:
        with open(file_path, "r") as fileobj:
            reader = csv.reader(fileobj)
            header = next(reader)
            data = {}

            for row in reader:
                data[row[0]] = {
                    "Rating": row[1],
                    "Year": row[2],
                    "Poster": row[3],
                }
            return data
    except FileNotFoundError:
        return {}


def write_csv_data(file_path, data):
    """Function so support writing .csv files after CRUD actions made,
     to safe latest version of .csv storage.
     Returns nothing. """

    with open(file_path, "w", newline="") as fileobj:
        writer = csv.writer(fileobj)
        writer.writerow(["Title", "Rating", "Year", "Poster"])

        for title, movie_data in data.items():
            writer.writerow([
                title,
                movie_data["Rating"],
                movie_data["Year"],
                movie_data["Poster"],
            ])


class StorageCSV(IStorage):
    """ Class inherits from class IStorage and handles listing, adding,
    deleting and updating movie information saved as .csv file.
    """

    def __init__(self, file_path):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            write_csv_data(self.file_path, {})

    def list_movies(self):
        """Class Method to fetch all existing movie records from
                .csv file storage, returns a dict of dicts."""

        return read_csv_data(self.file_path)

    def add_movie(self, title, rating, year, poster):
        """ Reads all existing movies, adds a new movie record as passed
        to the method and saves new movie record along with all records to .csv file"""

        data = read_csv_data(self.file_path)
        data[title] = {"Rating": rating, "Year": year, "Poster": poster}
        write_csv_data(self.file_path, data)

    def delete_movie(self, title):
        """Reads all existing movies, deletes a movie record as passed
        to the method and saves remaining movie records .csv file"""

        data = read_csv_data(self.file_path)

        if title in data:
            del data[title]

        write_csv_data(self.file_path, data)

    def update_movie(self, title, rating):
        """Reads all existing movies, updates a movie record as passed
        to the method and saves updated movie record along with existing records to .csv file"""

        data = read_csv_data(self.file_path)

        if title in data:
            data[title]["Rating"] = rating

        write_csv_data(self.file_path, data)