from istorage import IStorage
import csv
import os


class StorageCSV(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", newline="") as fileobj:
                writer = csv.writer(fileobj)
                writer.writerow(['Title', 'Rating', 'Year', 'Poster'])

    def list_movies(self):
        """ Lists all movies in the instantiated database."""

        with open(self.file_path, "r") as fileobj:
            reader = csv.reader(fileobj)

            data = {}

            next(reader)
            for line in reader:
                data[line[0]] = {'Rating':line[1], 'Year':line[2], 'Poster':line[3]}

            return data


    def add_movie(self, title, year, rating, poster):
        """ """

        with open(self.file_path, "r") as fileobj:
            reader = csv.reader(fileobj)
            existing_data = list(reader)

        with open(self.file_path, "w", newline="") as fileobj:
            writer = csv.writer(fileobj)
            writer.writerows(existing_data)
            writer.writerow([title, year, rating, poster])

    def delete_movie(self, title):
        """ Deletes a movie from the database"""

        with open(self.file_path, "r") as fileobj:
            reader = csv.reader(fileobj)

            list_of_movies = []

            for row in reader:
                list_of_movies.append(row)

            movie_index_to_be_removed = None

            for index, movie in enumerate(list_of_movies):
                if movie[0] == title:
                    movie_index_to_be_removed = index

            list_of_movies.pop(movie_index_to_be_removed)

            existing_data = list_of_movies

        with open(self.file_path, "w", newline="") as fileobj:
            writer = csv.writer(fileobj)
            writer.writerows(existing_data)


    def update_movie(self, title, rating):
        """ Updates the ranking of a movie"""


        with open(self.file_path, "r") as fileobj:
            reader = csv.reader(fileobj)

            list_of_movies = []

            title_index = 0
            rating_index = 1

            for row in reader:
                list_of_movies.append(row)

            movie_index_to_be_updated = None

            for index, movie in enumerate(list_of_movies):
                if movie[0] == title:
                    movie_index_to_be_updated = index

            list_of_movies[movie_index_to_be_updated][rating_index] = rating

            existing_data = list_of_movies

        with open(self.file_path, "w", newline="") as fileobj:
            writer = csv.writer(fileobj)
            writer.writerows(existing_data)