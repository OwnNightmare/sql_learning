import sqlalchemy
from pprint import pprint

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
    long_tracks = connection.execute("""SELECT track_name
        FROM Track
        WHERE duration > 210""").fetchall()
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


def count_artists_in_genre():
    artists_numbers = connection.execute("""SELECT genre_name AS genre,
     COUNT(a.artist_id) AS artists
     FROM genre g JOIN artists_genre a
     ON g.genre_id = a.genre_id
     GROUP BY genre_name
     ORDER BY genre_name ASC""").fetchall()
    return artists_numbers


def count_tracks_in_19_20():
    track_numbers = connection.execute("""SELECT COUNT(track_id) AS quantity 
    FROM track t JOIN album a 
    ON t.album_id = a.album_id
    WHERE a.release_year BETWEEN 2019 AND 2020""").fetchall()
    return track_numbers


def find_avg_duration():
    avg_duration = connection.execute("""SELECT AVG(duration) AS average_track_duration,
    a.album_name AS album
    FROM track t JOIN album a 
    ON t.album_id = a.album_id
    GROUP BY album
    ORDER BY album""").fetchall()
    return avg_duration


def get_not_in_2020():
    inactive_in_2020 = connection.execute("""SELECT distinct artist_name
    FROM artist a 
    JOIN artists_albums ab
        ON a.artist_id = ab.artist_id
    JOIN album al
        ON ab.album_id = al.album_id
    WHERE al.release_year <> 2020""").fetchall()
    return inactive_in_2020


if __name__ == '__main__':
    count_artists_in_genre()

