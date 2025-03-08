import statistics
import requests
import random
import os
from dotenv import load_dotenv

API_KEY = "f86d81ee"
URL = f"https://www.omdbapi.com/?apikey={API_KEY}"


class MovieApp:
    """ Class handles CLI. It's methods do represent the functionality and
    available features of the movie app.
    """

    def __init__(self, storage):
        self._storage = storage


    def _command_list_movies(self):
        """ Method calls instance storage and prints it's content
        in a readable format.
        """

        movies = self._storage.list_movies()

        titles = list(movies.keys())
        print()
        print(f"A total of {len(titles)} movies in your storage.")
        for title in titles:
            print(f"-  {title}")

    def _command_add_movie(self, title):
        """ Method sends get request to OMDb API and fetches movie data for
         the respective movie title as follows. After successful get request,
         the data is stored to the respective file by calling
         'add_movie' storage method.
        """

        try:
            query_string = f"&t={title}"
            response = requests.get(URL + query_string)
            response_json = response.json()

            if response_json['Response'] == "True":

                if response.status_code == 200:

                    title = response_json["Title"]
                    year = response_json["Year"]
                    imdb_rating = (
                        float(response_json["Ratings"][0]["Value"][:2]))
                    poster_link = response_json["Poster"]

                    self._storage.add_movie(title, imdb_rating, year,
                                            poster_link)
                    print(f"Movie {title} added successfully.")

                else:
                    print(f"Error: API returned status code "
                          f"{response.status_code}")

            else:
                print(f"({title}) --- {response_json['Error']}")


        except requests.exceptions.ConnectionError:
            print("Error: connection to OMDb API failed!")

    def _command_delete_movie(self, title):
        """ Method deletes respective title passed to it by calling
        storage method 'delete_movie'"""

        self._storage.delete_movie(title)


    def _command_movie_stats(self):
        """ Method calls sorage method 'list_movies' and
        calculates and then prints various statistics based on the movies
        stored.
        """

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
        """ Takes one random movie title from the storage
        and prints it.
        """

        movies = self._storage.list_movies()

        random_movie = random.choice(list(movies.keys()))

        print()
        print(f"Your film for tonight is '{random_movie}' --- Enjoy!!")
        print()

    def _command_search_movie(self):
        """ Prompts the user to enter a movie title (or only parts of it)
        and searches the storage for matching movie titles. In case there
        is one, it prints it to the screen.
        """

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
        """ Sorts all movies stored in descending order
        according to it's IMDb score. """

        movies = self._storage.list_movies()

        sorted_movies_dict = dict(
            sorted(movies.items(), key=lambda item: item[1]['Rating'],
                   reverse=True)
        )

        index = 1
        print()
        for movie, info in sorted_movies_dict.items():
            print(f"TOP {index}: Movie: {movie} (IMDb rating: {info['Rating']})")
            index += 1
        print()

    def _generate_website(self):
        """ Method takes stored movies and formats it to
        html code, reads an existing html template and replaces a placeholder
        with the formatted movies content. Then saves all the html code
        to an 'index.html' file which then can be loaded in the browser to view.
        """

        movies = self._storage.list_movies()

        movies_website_content = ""

        if movies:

            for movie, info in movies.items():
                movies_website_content += f'<li>\n'
                movies_website_content += f'<div class="movie">\n'
                movies_website_content += (f'<img class="movie-poster" '
                                           f'src={info['Poster']} title>\n')
                movies_website_content += (f'<div class="movie-title">{movie}'
                                           f'</div>\n')
                movies_website_content += (f'<div class="movie-year">'
                                           f'{info['Year']}</div>\n')
                movies_website_content += f'</div>\n'
                movies_website_content += f'</li>\n'


        with open("_static/index_template.html", "r") as fileobj:
            page_content = fileobj.readlines()

            html_content_as_string = ""

            for line in page_content:
                html_content_as_string += f"{line}\n"

        html_with_dynamic_content = (html_content_as_string.replace
                                     ("__TEMPLATE_MOVIE_GRID__",
                                      movies_website_content))

        with open("templates/index.html", "w") as fileobj:
            fileobj.write(html_with_dynamic_content)

        print("Website generated successfully.")

    def run(self):
        """ Method consists of a while loop, taking care of an
        appropriate user experience through the CLI and calls
        methods above according to what the user enters to the CLI.
        """

        movies = self._storage.list_movies()

        while True:
            print(
                """

            ********** Welcome to NETFLIX (FÜR ARME) **********

            Menu:

            0.  Exit
            1.  List movies
            2.  Add movie
            3.  Delete Movie
            4.  Update movie
            5.  Stats
            6.  Random movie
            7.  Search movie
            8.  Movies sorted by ranking
            9.  Generate Website
            """
            )

            users_selection = input("\nEnter choice (0-8): ")

            if users_selection == "0":
                print("Bye!")
                break

            elif users_selection == "1":

                MovieApp._command_list_movies(self)

                move_on = input("\nPress enter to move on\n")
                if move_on == "":
                    continue


            elif users_selection == "2":

                movie_to_add = input("\nPlease enter a movie you want to add: ")

                if movie_to_add not in movies.keys():
                    MovieApp._command_add_movie(self, movie_to_add)

                else:
                    print(f"\n{movie_to_add} already exists in your storage.\n")

                move_on = input("\nPress enter to move on\n")

                if move_on == "":
                    continue

            elif users_selection == "3":

                movie_to_delete = input("Enter a movie name to delete: ")

                if movie_to_delete in movies.keys():
                    MovieApp._command_delete_movie(self, movie_to_delete)
                    print(f"\n{movie_to_delete} successfully deleted from "
                          f"your storage.")

                else:
                    print(f"\nMovie '{movie_to_delete}' was not found in "
                          f"your storage.")

                move_on = input("\nPress enter to move on\n")
                if move_on == "":
                    continue

            elif users_selection == "4":

                print("Soorryyy but option 4 is currently under construction")

                move_on = input("Press enter to move on")
                if move_on == "":
                    continue

            elif users_selection == "5":

                MovieApp._command_movie_stats(self)

                move_on = input("\nPress enter to move on\n")
                if move_on == "":
                    continue

            elif users_selection == "6":

                MovieApp._command_random_movie(self)

                move_on = input("Press enter to move on")
                if move_on == "":
                    continue

            elif users_selection == "7":

                MovieApp._command_search_movie(self)

                move_on = input("Press enter to move on")
                if move_on == "":
                    continue

            elif users_selection == "8":

                MovieApp._command_sort_movies_by_rating(self)

                move_on = input("Press enter to move on")
                if move_on == "":
                    continue

            elif users_selection == "9":

                MovieApp._generate_website(self)
                print("\nTo open your movies website:")
                print("step 1 - go to folder 'templates'")
                print("step 2 - open file 'index.html'")
                print("step 3 - open the file via IDE built-in pre-view or "
                      "open local url in your browser(e.g. Chrome)\n")

                move_on = input("Press enter to move on")
                if move_on == "":
                    continue