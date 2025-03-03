from movie_app import MovieApp
from storage_json import StorageJson

storage = StorageJson('movies.json')
movie_app = MovieApp(storage)
movie_app._command_list_movies()
movie_app._command_movie_stats()


