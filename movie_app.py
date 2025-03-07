import statistics
import requests
import random
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

        try:
            query_string = f"&t={title}"
            response = requests.get(URL + query_string)
            response_json = response.json()

            if response_json['Response'] == "True":

                if response.status_code == 200:

                    title = response_json["Title"]
                    year = response_json["Year"]
                    imdb_rating = float(response_json["Ratings"][0]["Value"][:2])
                    poster_link = response_json["Poster"]

                    self._storage.add_movie(title, imdb_rating, year, poster_link)
                    print(f"Movie {title} added successfully.")

                else:
                    print(f"Error: API returned status code {response.status_code}")

            else:
                print(f"({title}) --- {response_json['Error']}")


        except requests.exceptions.ConnectionError:
            print("Error: connection to OMDb API failed!")

    def _command_delete_movie(self, title):

        self._storage.delete_movie(title)


    def _command_movie_stats(self):
        movies = self._storage.list_movies()

        sum_of_values = 0

        movies_dict = {}

        for movie, info in movies.items():
            movies_dict[movie] = info["Rating"]

        for rating in movies_dict.values():
            sum_of_values += float(rating)
            average_rating = sum_of_values / len(movies_dict)
        print(f"\nAverage rating: {average_rating}")

        median_rating = statistics.median(map(float, movies_dict.values()))
        print(f"Median rating: {median_rating}")

        max_rank = max(movies_dict, key=movies_dict.get)
        print(f"Best rating -> {max_rank}: {movies_dict[max_rank]}")

        min_rank = min(movies_dict, key=movies_dict.get)
        print(f"Worst rating-> {min_rank}: {movies_dict[min_rank]}")
        print()
    def _command_random_movie(self):
        movies = self._storage.list_movies()

        random_movie = random.choice(list(movies.keys()))

        print()
        print(f"Your film for tonight is '{random_movie}' --- Enjoy!!")
        print()

    def _command_search_movie(self):
        movies = self._storage.list_movies()

        movie_to_search_part = input("Enter part of movie name: ")

        if movie_to_search_part != "":
            if movie_to_search_part.lower() in str(movies.keys()).lower():
                for movie, info in movies.items():
                    if movie_to_search_part.lower() in movie.lower():
                        print(f"{movie} (IMDb: {info['Rating']})")
                print()

            else:
                print(f"\nNo results found for '{movie_to_search_part}'.\n")

        else:
            print("This field cannot be empty!")


    def _command_sort_movies_by_rating(self):
        movies = self._storage.list_movies()

        sorted_movies_dict = dict(
            sorted(movies.items(), key=lambda item: item[1]['Rating'], reverse=True)
        )

        index = 1
        print()
        for movie, info in sorted_movies_dict.items():
            print(f"TOP {index}: Movie: {movie} (IMDb rating: {info['Rating']})")
            index += 1
        print()

    def _generate_website(self):
        movies = self._storage.list_movies()

        movies_website_content = ""

        if movies:

            for movie, info in movies.items():
                movies_website_content += f'<li>\n'
                movies_website_content += f'<div class="movie">\n'
                movies_website_content += f'<img class="movie-poster" src={info['Poster']} title>\n'
                movies_website_content += f'<div class="movie-title">{movie}</div>\n'
                movies_website_content += f'<div class="movie-year">{info['Year']}</div>\n'
                movies_website_content += f'</div>\n'
                movies_website_content += f'</li>\n'


        with open("_static/index_template.html", "r") as fileobj:
            page_content = fileobj.readlines()

            html_content_as_string = ""

            for line in page_content:
                html_content_as_string += f"{line}\n"

        html_with_dynamic_content = html_content_as_string.replace("__TEMPLATE_MOVIE_GRID__", movies_website_content)

        with open("templates/index.html", "w") as fileobj:
            fileobj.write(html_with_dynamic_content)

        print("Website generated successfully.")

    def run(self):
        pass
      # Print menu
      # Get use command
      # Execute command