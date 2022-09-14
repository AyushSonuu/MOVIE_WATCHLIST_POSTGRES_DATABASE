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