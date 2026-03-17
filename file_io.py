import json


def read_movies(file_name):
    """Reads movies from JSON file and returns a list"""

    try:
        with open(file_name, 'r') as fh:
            return json.load(fh)

    except FileNotFoundError:
        print("The movie database does not exist")
        return []


def write_movies(file_name, movies):
    """Collect Movie Data and Write a file"""

    with open(file_name, 'w') as fh:
        json.dump(movies, fh, indent=4)

