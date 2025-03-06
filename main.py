from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV

storage = StorageJson('movies.json')
storage2 = StorageCSV('movies.csv')
movie_app = MovieApp(storage2)




movie_app._command_delete_movie("Titanic")

print(storage2.list_movies())



