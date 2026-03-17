import sys
import file_io
import movie_manager


def main():
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

        if option == "a":
            movie_manager.add_movie(file_name, movies)

        elif option == "d":
            movie_manager.delete_movie(file_name, movies)

        elif option == "s":
            movie_manager.view_summary(file_name)

        elif option == "r":
            print("Search by Rating")

        elif option == "t":
            print("Search by title")

        elif option == "g":
            print("Search by Genre")

        elif option == "q":
            print("You've exited the program")
            break


if __name__ == "__main__":
    main()
