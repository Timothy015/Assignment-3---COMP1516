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
        print("a - Add Movie"
              "\nd - Delete Movie"
              "\ns - View Movie Summary"
              "\nr - Search by Rating"
              "\nt - Search by Title"
              "\ng - Search by Genre"
              "\nq - Quit")

        option = input("Select an option: ").strip().lower()

        if option == "a":
            movie_manager.add_movie(file_name, movies)

        elif option == "d":
            movie_manager.delete_movie(file_name, movies)

        elif option == "s":
            print("View Summary")

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
