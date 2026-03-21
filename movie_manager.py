import file_io
import re


def add_movie(file_name, movies):
    """Add Movies and check with the criteria"""
    title = input("Title: ")
    if re.search(r"^[A-Za-z0-9 ]{1,32}$", title) is None:
        raise ValueError("Title must be no longer than 32 Characters")

    for movie in movies:
        if movie["title"].lower() == title.lower():
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
        rating = int(input("Rating: "))
    except ValueError:
        raise ValueError("Rating must be a number")

    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 and 5")

    description = input("Description: ")
    if len(description) > 128:
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


def view_summary(movies):
    """Opens JSON file and prints to console"""

    if len(movies) == 0:
        print("No Movies Yet")

    else:
        for movie in movies:
            description = movie['description'][:30]

            print(
                f"Title: {movie['title']} "
                f"Genre: {movie['genre']} "
                f"Length: {movie['length']} "
                f"Year: {movie['year']} "
                f"Rating: {movie['rating']} "
                f"Description: {description} "
                )


def rating_search(movies):
    """Searches JSON File by rating"""
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
            description = movie['description'][:30]
            print(
                f"Title: {movie['title']} "
                f"Genre: {movie['genre']} "
                f"Length: {movie['length']} "
                f"Year: {movie['year']} "
                f"Rating: {movie['rating']} "
                f"Description: {description} "
            )

    if not found:
        print("No movies found with that rating")


def title_search(movies):
    """Searches JSON File by Title"""

    title = input("Enter the Movie Title: ").strip()

    found = False
    for movie in movies:
        if title.lower() in movie["title"].lower():
            found = True
            print(
                f"Title: {movie['title']} "
                f"Genre: {movie['genre']} "
                f"Length: {movie['length']} "
                f"Year: {movie['year']} "
                f"Rating: {movie['rating']} "
                f"Description: {movie["description"]} "
            )

    if not found:
        print("Movie not found")


def genre_search(movies):
    """Searches JSON file by Genre"""

    genre = input("Enter the genre: ").strip()

    found = False
    for movie in movies:
        if genre.lower() in movie["genre"].lower():
            found = True
            print(
                f"Title: {movie['title']} "
                f"Genre: {movie['genre']} "
                f"Length: {movie['length']} "
                f"Year: {movie['year']} "
                f"Rating: {movie['rating']} "
                f"Description: {movie['description']} "
            )

    if not found:
        print("Movie not found")
