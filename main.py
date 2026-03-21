import sys
import file_io
import movie_manager


def main():
    """Runs Movie Manager
    Handles command line arguments, displays the menu,
    and processes user input until the user quits"""

    if len(sys.argv) != 2:
        print("Usage: python movie_manager.py movie.json")
        return

    file_name = sys.argv[1]
    movies = file_io.read_movies(file_name)

    while True:
        print("Add Movie (a)"
              "\nDelete Movie (d)"
              "\nView Movie Summary (s)"
              "\nSearch by Rating (r)"
              "\nSearch by Title (t)"
              "\nSearch by Genre (g)"
              "\nQuit (q)")

        option = input("Select an option: ").strip().lower()
        try:
            if option == "a":
                movie_manager.add_movie(file_name, movies)

            elif option == "d":
                movie_manager.delete_movie(file_name, movies)

            elif option == "s":
                movies = file_io.read_movies(file_name)
                movie_manager.view_summary(movies)

            elif option == "r":
                movies = file_io.read_movies(file_name)
                movie_manager.rating_search(movies)

            elif option == "t":
                movies = file_io.read_movies(file_name)
                movie_manager.title_search(movies)

            elif option == "g":
                movies = file_io.read_movies(file_name)
                movie_manager.genre_search(movies)

            elif option == "q":
                print("You've exited the program")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
