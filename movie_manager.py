import json
import file_io
import re


def add_movie(file_name, movies):

    title = input("Title: ")
    genre = input("Genre: ")
    length = input("Length (HH:MM): ")
    year = input("Year: ")
    rating = input("Rating: ")
    description = input("Description: ")

    movie = {
        "title": title,
        "genre": genre,
        "length": length,
        "year": int(year),
        "rating": float(rating),
        "description": description
    }

    movies.append(movie)

    file_io.write_movies(file_name, movies)

    print("Movie added successfully")


def delete_movie(file_name, movies):
    """Deletes Movie from JSON file"""

    title = input("Enter movie title to delete: ")

    for movie in movies:
        if movie["title"].lower() == title.lower():
            movies.remove(movie)
            file_io.write_movies(file_name, movies)
            print("Movie deleted successfully")
            return

    print("Movie not Found!")


def view_summary(file_name):
    """Opens JSON file and prints to console"""

    with open(file_name, 'r') as fh:
        summary = json.load(fh)
    print(summary)