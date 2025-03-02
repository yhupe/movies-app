from movie_app import MovieApp
from storage_json import StorageJson

storage = StorageJson('movies.json')
storage.add_movie("Hannes", 1996, 10, "loco")
movie_app = MovieApp(storage)
print(movie_app._command_list_movies())
