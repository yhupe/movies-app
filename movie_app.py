import statistics
import requests
import os
from dotenv import load_dotenv

API_KEY = "f86d81ee"
URL = f"https://www.omdbapi.com/?apikey={API_KEY}"


class MovieApp:
    def __init__(self, storage):
        self._storage = storage


    def _command_list_movies(self):
        movies = self._storage.list_movies()

        titles = list(movies.keys())

        for title in titles:
            print(title)

    def _command_add_movie(self, title):

        query_string = f"&t={title}"
        response = requests.get(URL + query_string)
        response_json = response.json()

        title = response_json["Title"]
        year = response_json["Year"]
        imdb_rating = response_json["Ratings"][0]["Value"]
        poster_link = response_json["Poster"]

        self._storage.add_movie(title, year, imdb_rating, poster_link)

    def _command_delete_movie(self, title):

        self._storage.delete_movie(title)


    def _command_movie_stats(self):
        movies = self._storage.list_movies()

        sum_of_values = 0

        movies_dict = {}

        for movie, info in movies.items():
            movies_dict[movie] = info["Rating"]

        for rating in movies_dict.values():
            sum_of_values += rating
            average_rating = sum_of_values / len(movies_dict)
        print(f"\nAverage rating: {average_rating}")

        print(f"Median rating: {statistics.median(movies_dict.values())}")

        max_rank = max(movies_dict, key=movies_dict.get)
        print(f"Best rating -> {max_rank}: {movies_dict[max_rank]}")

        min_rank = min(movies_dict, key=movies_dict.get)
        print(f"Worst rating-> {min_rank}: {movies_dict[min_rank]}")
        print()

    def _generate_website(self):
        pass

    def run(self):
        pass
      # Print menu
      # Get use command
      # Execute command