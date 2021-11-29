import sqlalchemy
from pprint import pprint
import pandas as pd

"""Функции данного модуля вызываются в файле 'select_runner.py'"""


db = 'postgresql://me:password@localhost:5432/my_db'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


def get_albums():
    albums2018 = connection.execute("""SELECT album_name AS album, 
        release_year AS release
        FROM Album
        WHERE release_year = 2018
        ORDER BY release_year DESC
        """).fetchall()
    pprint(albums2018)


def get_longest():
    longest = connection.execute("""SELECT track_name, duration 
        FROM Track
        ORDER BY duration DESC
        LIMIT 1""").fetchall()
    pprint(longest)


def get_long_tracks():
    long_tracks = pd.read_sql("""SELECT track_name as track
        FROM Track
        WHERE duration > 210""", con=connection)
    pprint(long_tracks)


def get_one_worded():
    one_worded = connection.execute("""SELECT artist_name
        FROM Artist
        WHERE TRIM (TRAILING ' ' FROM artist_name) NOT LIKE '%% %%' 
        """).fetchall()
    pprint(one_worded)


def get_with_my():
    includes_my = connection.execute("""SELECT track_name
        FROM Track
        WHERE track_name iLIKE '%% my %%' 
        or track_name iLIKE '%% мой %%' """).fetchall()
    pprint(includes_my)


def get_mix_in_18_20():
    between18_20 = connection.execute("""SELECT mixtape_name 
        FROM Mixtape
        WHERE release_year BETWEEN 2018 and 2020""").fetchall()
    pprint(between18_20)


# Complex selects:
def count_artists_in_genre():
    artists_numbers = pd.read_sql("""SELECT genre_name AS genre,
        COUNT(a.artist_id) AS artists
        FROM genre g JOIN artists_genre a
            ON g.genre_id = a.genre_id
        GROUP BY genre_name
        ORDER BY genre_name ASC""", connection)
    return artists_numbers


def count_tracks_in_19_20():
    track_numbers = pd.read_sql("""SELECT COUNT(track_id) AS tracks 
        FROM track t JOIN album a 
            ON t.album_id = a.album_id
        WHERE a.release_year BETWEEN 2019 AND 2020""", connection)
    return track_numbers


def find_avg_duration():
    avg_duration = pd.read_sql("""SELECT album_name AS album, 
        AVG(duration) AS avg_duration
        FROM track t JOIN album a 
            ON t.album_id = a.album_id
        GROUP BY album
        ORDER BY album""", connection)
    return avg_duration


def get_not_in_2020():
    inactive_in_2020 = pd.read_sql("""SELECT distinct artist_name AS artist
        FROM artist a 
        JOIN artists_albums ab
            ON a.artist_id = ab.artist_id
        JOIN album al
            ON ab.album_id = al.album_id
        WHERE al.release_year <> 2020""", connection)
    return inactive_in_2020


def get_mix_with_maneskin():
    mixes = pd.read_sql("""SELECT mixtape_name AS mixtape
        FROM mixtape m JOIN trackmixtape tm 
            ON m.mixtape_id = tm.mixtape_id
        JOIN track t 
            ON tm.track_id = t.track_id
        JOIN artists_albums ab
            ON t.album_id = ab.album_id
        WHERE ab.artist_id = 1""", connection)
    return mixes


def get_feated_albums():
    alb = pd.read_sql("""SELECT album_name album
        FROM album a JOIN artists_albums aa
            ON a.album_id = aa.album_id
        JOIN artists_genre ag
            ON aa.artist_id = ag.artist_id
        GROUP BY album_name 
        HAVING COUNT(distinct ag.genre_id) > 1""", connection)
    return alb


def get_not_in_mixes():
    excluded = pd.read_sql("""SELECT track_name AS track
        FROM track t left JOIN trackmixtape tm
            ON t.track_id = tm.track_id
        WHERE tm.track_id IS NULL""", connection)
    return excluded


def get_shortest_tracks():
    shortest = pd.read_sql("""SELECT artist_name artist, track_name track, duration
        FROM track t JOIN artists_albums aa
            ON t.album_id = aa.album_id
        JOIN artist a
            ON aa.artist_id = a.artist_id
        WHERE duration = (SELECT MIN(duration) FROM track)""", connection)
    return shortest


def get_shortest_albums():
    sh_al = pd.read_sql("""SELECT album_name album
        FROM album a JOIN track t
            ON  a.album_id = t.album_id
        GROUP BY album_name
        HAVING COUNT(track_id) = (SELECT COUNT(track_id)
            FROM track t JOIN album a
                ON t.album_id = a.album_id 
            GROUP BY album_name
            LIMIT 1)""", connection)
    return sh_al

