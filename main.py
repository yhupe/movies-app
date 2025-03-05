from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV

storage = StorageJson('movies.json')
storage2 = StorageCSV('movies.csv')
movie_app = MovieApp(storage2)

storage2.add_movie("Movie1", 2025, 1000, "Poster")
storage2.add_movie("Movie2", 2026, 1000, "Poster")
storage2.add_movie("Movie3", 2027, 1000, "Poster")
storage2.update_movie("Movie1", 999)
print(storage2.list_movies())

