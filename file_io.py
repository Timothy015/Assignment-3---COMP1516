import json
import os


def read_movies(file_name):
    """Reads movies from JSON file and returns a list"""
    if not os.path.exists(file_name):
        print("The movie database does not exist")
        return []

    with open(file_name, 'r') as fh:
        return json.load(fh)


def write_movies(file_name, movies):
    """Collect Movie Data and Write a file"""

    with open(file_name, 'w') as fh:
        json.dump(movies, fh, indent=4)

