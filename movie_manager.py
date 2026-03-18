import json
import file_io
import re


def add_movie(file_name, movies):
    """Add Movies and check with the criteria"""
    title = input("Title: ")
    if re.search(r"^[A-Z][a-z0-9]{1,32}$", title) is None:
        raise ValueError("Title must be no longer than 32 Characters")

    for title in movies:
        if movies["title"].lower() == title.lower():
            raise ValueError("Movie already exists")

    genre = input("Genre: ")
    if re.search(r"^[A-Z] ?[a-z]*$", genre) is None:
        raise ValueError("Genre is invalid")

    length = input("Running Length (HH:MM): ")
    if re.search(r"^\d{2}:[0-5]\d$", length) is None:
        raise ValueError("Length must be in HH:MM format (00-99:00-59)")

    year = input("Year: ")
    if re.search(r"^\d{4}$", year) is None:
        raise ValueError("Year is invalid")

    if re.search(r"^\d+$", year) is None:
        raise TypeError("Year must be an integer")

    try:
        rating = float(input("Rating: "))
    except ValueError:
        raise ValueError("Rating must be a number")

    if rating < 0 or rating > 5:
        raise ValueError("Rating must be between 0 and 5")

    description = input("Description: ")
    if len(description) > 128:
        raise ValueError("Description must be 128 characters or less")

    movie = {
        "title": title,
        "genre": genre,
        "length": length,
        "year": year,
        "rating": rating,
        "description": description
    }

    movies.append(movie)

    file_io.write_movies(file_name, movies)

    print("Movie added successfully")


def delete_movie(file_name, movies):
    """Deletes Movie from JSON file"""
    movie_to_delete = input("Enter the name of the movie: ")

    is_deleted = False
    for movie in movies:
        if movie["title"].lower() == movie_to_delete.lower():
            movies.remove(movie)
            is_deleted = True
            break
    if is_deleted:
        file_io.write_movies(file_name, movies)
        print("Movie Deleted")
    else:
        print("Movie not Found")


def view_summary(file_name):
    """Opens JSON file and prints to console"""

    with open(file_name, 'r') as fh:
        summary = json.load(fh)
    print(summary)


def rating_search():
    """Searches JSON File by rating"""
    pass


def title_search():
    """Searches JSON File by Title"""
    pass


def genre_search():
    """Searches JSON file by Genre"""
    pass
