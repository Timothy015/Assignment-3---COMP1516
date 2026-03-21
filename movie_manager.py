import file_io
import re


def add_movie(file_name, movies):
    """Prompts user to add a new movie
    :param file_name: The JSON file name
    :param movies: The current list of movies"""

    title = input("Title: ")
    if len(title) == 0 or len(title) > 32:
        raise ValueError("Title must be 1-32 Characters")

    for movie in movies:
        if movie["title"].lower() == title.lower():
            raise ValueError("Movie already exists")

    genre = input("Genre: ")
    if not genre.strip() or re.search(r"^[A-Za-z ]+$", genre) is None:
        raise ValueError("Genre must contain only letters and spaces")

    length = input("Running Length (HH:MM): ")
    if re.search(r"^\d{2}:[0-5]\d$", length) is None:
        raise ValueError("Length must be in HH:MM format (00-99:00-59)")

    year = input("Year: ")
    if re.search(r"^\d{4}$", year) is None:
        raise ValueError("Year must be 4 digits")

    if int(year) <= 1920:
        raise ValueError("Year must be greater than 1920")

    try:
        rating = int(input("Rating: "))
    except ValueError:
        raise ValueError("Rating must be a number")

    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 and 5")

    description = input("Description: ")
    if len(description) == 0 or len(description) > 128:
        raise ValueError("Description must be 128 characters or less")

    new_movie = {
        "title": title,
        "genre": genre,
        "length": length,
        "year": year,
        "rating": rating,
        "description": description
    }

    movies.append(new_movie)

    file_io.write_movies(file_name, movies)

    print("Movie added successfully")


def delete_movie(file_name, movies):
    """Deletes a movie from the list based on title
    :param file_name: The JSON file name
    :param movies: The current list of movies"""

    movie_to_delete = input("Enter the name of the movie: ")

    if len(movie_to_delete) == 0 or len(movie_to_delete) > 32:
        raise ValueError("Title must be 1-32 characters")

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


def view_summary(movies):
    """Displays a summary of all movies
    :param movies: The list of movies"""

    if len(movies) == 0:
        print("No Movies Yet")

    else:
        for movie in movies:
            description = movie['description'][:30]

            print(
                f"Title:{movie['title']}, "
                f"Genre:{movie['genre']}, "
                f"Length:{movie['length']}, "
                f"Year:{movie['year']}, "
                f"Rating:{movie['rating']}, "
                f"Description:{description} "
            )


def rating_search(movies):
    """Searches for movies by minimum rating
    :param movies: The list of movies"""

    try:
        minimum_rating = int(input("Enter the rating: "))
    except ValueError:
        raise ValueError("Rating must be a whole number")

    if minimum_rating < 1 or minimum_rating > 5:
        raise ValueError("Rating must be between 1 and 5")

    found = False
    for movie in movies:
        if movie['rating'] >= minimum_rating:
            found = True
            print(
                f"Title:{movie['title']}, "
                f"Genre:{movie['genre']}, "
                f"Length:{movie['length']}, "
                f"Year:{movie['year']}, "
                f"Rating:{movie['rating']}, "
                f"Description:{movie['description']} "
            )

    if not found:
        print("No movies found with that rating")


def title_search(movies):
    """Searches for movies by Title
    The search is case-insensitive and allows partial matches
    :param movies: The list of movies"""

    title = input("Enter the Movie Title: ").strip()

    found = False
    for movie in movies:
        if title.lower() in movie["title"].lower():
            found = True
            print(
                f"Title:{movie['title']}, "
                f"Genre:{movie['genre']}, "
                f"Length:{movie['length']}, "
                f"Year:{movie['year']}, "
                f"Rating:{movie['rating']}, "
                f"Description:{movie['description']} "
            )

    if not found:
        print("Movie not found")


def genre_search(movies):
    """Searches for movies by Genre
    The search is case-sensitive and allows partial matches
    :param movies: The list of movies"""

    genre = input("Enter the genre: ").strip()

    if not genre:
        raise ValueError("Genre cannot be empty")

    found = False

    for movie in movies:
        if genre in movie["genre"]:
            found = True
            print(
                f"Title:{movie['title']}, "
                f"Genre:{movie['genre']}, "
                f"Length:{movie['length']}, "
                f"Year:{movie['year']}, "
                f"Rating:{movie['rating']}, "
                f"Description:{movie['description']} "
            )

    if not found:
        print("Movie not found")
