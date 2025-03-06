from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV

storage = StorageJson('movies.json')
storage2 = StorageCSV('movies.csv')
movie_app = MovieApp(storage)

movie_app._command_add_movie("Titanic")
movie_app._command_add_movie("James Bond")
movie_app._command_add_movie("Joker")

movie_app._command_movie_stats()


