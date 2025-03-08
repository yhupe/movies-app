from movie_app import MovieApp
from storage.storage_json import StorageJson
from storage.storage_csv import StorageCSV


# Instantiating storage files for .csv / .json
storage_json = StorageJson('storage/user_data/movies.json')
storage_csv = StorageCSV('storage/user_data/movies.csv')

# Instantiating movie apps based on the storage file created earlier
movie_app_json = MovieApp(storage_json)
movie_app_csv = MovieApp(storage_csv)

# Calling MovieApp.run() to start the application
def main():
    movie_app_csv.run()

if __name__ == '__main__':
    main()