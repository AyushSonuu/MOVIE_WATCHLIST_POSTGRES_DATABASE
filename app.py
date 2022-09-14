import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()

def prompt_add_movies():
    title = input("movie title : ")
    release_date = input("Realease date (dd-mm-yy): ")
    parsed_date = datetime.datetime.strptime(release_date,"%d-%m-%y")
    timestramp = parsed_date.timestamp()

    database.add_movies(title , timestramp)

def print_movie_list(heading ,movies):
    print(f"--{heading } movies--")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %y")
        print(f"{_id} : {title} release on {human_date}")
    print("----\n")

# def print_watched_movies_list(username,movies):
#     print(f"--{username}'s watched movies--")
#     for movie in movies:
#         print(f"{movie[1]}")
#     print("----\n")

def prompt_watch_movie():
    username = input("Username : ")
    movie_id = input("movie_id")
    database.watch_movies(username,movie_id)

def prompt_add_user():
    username = input("username : ")
    database.add_user(username)

def prompt_show_watched_movies():
    username = input("username : ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list(f"{username}'s watched movies", movies)
    else:
        print("this user had not watched anything yet!")

def prompt_search_movies():
    search_term = input("Enter partial movie title")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("movies found",movies)
    else:
        print("found no movies for that search term")


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movies()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("upcomming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("all",movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
       prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")