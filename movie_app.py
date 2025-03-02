class MovieApp:
    def __init__(self, storage):
        self._storage = storage


    def _command_list_movies(self):
        movies = self._storage.list_movies()

        film_info = ""

        for movie in movies:
            film_info += f"Film title: {movie["Film name"]}\n"
            film_info += f"Film rating: {movie["Rating"]}\n"
            film_info += f"Year: {movie["Year"]}\n"
            film_info += f"Poster: {movie["Poster"]}\n"

        return film_info

    def _command_add_movie(self):
        movies = self._storage.add_movies()
        pass

    def _command_delete_movie(self):
        movies = self._storage.delete_movies()
        pass

    def _command_update_movie(self):
        movies = self._storage.update_movies()
        pass

    def _command_movie_stats(self):
        pass

    def _generate_website(self):
        pass

    def run(self):
        pass
      # Print menu
      # Get use command
      # Execute command