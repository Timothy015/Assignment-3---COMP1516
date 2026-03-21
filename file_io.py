import json
import os


def read_movies(file_name):
    """Reads movies data from JSON File
    :param file_name: The name of the file to read from
    :return: A list of movie dictionaries"""

    if not os.path.exists(file_name):
        print("The movie database does not exist")
        return []

    try:
        with open(file_name, 'r') as fh:
            return json.load(fh)

    except FileNotFoundError:
        return []


def write_movies(file_name, movies):
    """Writes movie data to JSON file
    :param file_name: The name of the file to write to
    :param movies: The list of movie dictionaries"""

    with open(file_name, 'w') as fh:
        json.dump(movies, fh, indent=4)
