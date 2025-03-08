from abc import ABC, abstractmethod


class IStorage(ABC):
    """ Abstract class (parent) for handling storage of different data types,
    for example .csv and .json files.
    """

    @abstractmethod
    def list_movies(self):
        """ Inheriting classes return a dictionary of dictionaries
        from the respective data type.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """ Inheriting classes are adding movie information as included in
        the arguments as a new movie to the respective data type.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """ Inheriting classes are adding movie information as included in
        the arguments as a new movie to the respective data type.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """ Inheriting classes are updating movie information as included in
        the arguments to an existing movie as the respective data type.
        """
        pass

