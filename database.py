# title , release_date, watched
import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEST,
    release_timestramp REAL

);
"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_name text,
    movie_id INTEGER,
    FOREIGN KEY (user_name) REFERENCES users(username),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
    );"""

INSERT_MOVIES = """INSERT INTO movies (
    title, 
    release_timestramp)
    VALUES (?,?); """

INSERT_USER = "INSERT INTO users (username) values (?)"

SELECT_ALL_MOVIES = "SELECT * FROM movies;"

SELECT_UPCOMMING_MOVIES = """SELECT * FROM movies 
                                WHERE release_timestramp > ?;"""

SELECT_WATCHED_MOVIES = """SELECT movies.*
                            FROM movies
                            JOIN watched ON movies.id = watched.movie_id
                            WHERE  user_name = ?;"""

SET_MOVIES_WATCHED = """UPDATE movies SET watched = 1
                            WHERE title = ?;"""

DELETE_MOVIE = "DELET FROM movies WHERE title = ?"

INSERT_WATCHED_MOVIE = """INSERT INTO watched (user_name,movie_id) values (?,?)"""

SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE ?"

connection = sqlite3.connect("data.db")
CREATE_RELEASE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_release on movies(release_timestramp);"


# connection.row_factory = sqlite3.Row

def create_tables():
    '''helps in creating the table'''
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)


def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))


def add_movies(title, release_timestramp):
    '''adds movie to the database'''
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestramp))


def get_movies(upcomming=False):
    '''gives all the upcomming movies and
    if upcomming = True then gives only the movies present in the database
    '''
    with connection:
        cursor = connection.cursor()
        if upcomming == True:
            today_timestramp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMMING_MOVIES, (today_timestramp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def search_movies(search_term):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIES, (f"%{search_term}%",))
        return cursor.fetchall()


def watch_movies(username, movie_id):
    '''takes the movie title and marks it as watched'''
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    '''gives the list of movies that have been watched'''
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()