from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV


# Instantiating storage files for .csv / .json
storage_json = StorageJson('movies.json')
storage_csv = StorageCSV('movies.csv')

# Instantiating movie apps based on the storage file created earlier
movie_app_json = MovieApp(storage_json)
movie_app_csv = MovieApp(storage_csv)

# Calling MovieApp.run() to start the application
movie_app_csv.run()






