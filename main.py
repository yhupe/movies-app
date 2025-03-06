from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV

storage_json = StorageJson('movies.json')
storage_csv = StorageCSV('movies.csv')
movie_app_json = MovieApp(storage_json)
movie_app_csv = MovieApp(storage_csv)




movie_app_csv._command_add_movie("Halt die schnauze")




