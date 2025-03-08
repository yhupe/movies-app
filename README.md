
# MOVIE MADNESS

## Description

'Movie Madness' is one of the countless small coding exercises I've completed during my awesome journey to become a software developer! This is the 3rd version so far - developing further and further. 

With 'Movie Madness' and the help of OOP, you are able to create different 'accounts' for saving your favourite movie titles in either .csv or .json format. 
Via the OMDb API, information like 'IMDb rating', 'year' and a link to the movie poster are fetched and added to your personal storage. You can also delete, update, and display all the titles in your storage. Some other features are the calculation of some statistics, sorting in descending order by the IMDb rating and the newest feature: the generation of a local url website with a graphic interface whehre you now can see your favourite movies library, besides to the command line interface. 

## How to install

To install the project, simply install the packages I used, as refered to in the requirements.txt:

```bash
pip install -r requirements
```

## How to use

Open the main.py file: Please instantiate a storage file with with either StorageJson() or StorageCSV() as you prefer it. In the parentheses, please put the name you want to give it. 
With that being done, please instatiate your movie app with MovieApp('your storage instance') and simply run the application with the .run() ending after your application instance, as shown below. Further instructions will be shown in the CLI.

```python
# Instantiating storage files for .csv / .json
storage_json = StorageJson('movies.json')
storage_csv = StorageCSV('movies.csv')

# Instantiating movie apps based on the storage file created earlier
movie_app_json = MovieApp(storage_json)
movie_app_csv = MovieApp(storage_csv)

# Calling MovieApp.run() to start the application
movie_app_csv.run()
```

## 🤙🏼
