import sqlalchemy

db = 'postgresql://me:password@localhost:5432/newdb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


def insert_artist():
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('James Blunt')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('Scorpions')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('Scriptonit')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('Fio Rida')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES ('Imagine Dragons')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('Twenty one pistols')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('OneRepublic')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('Ed Sheeran')
    ON CONFLICT DO NOTHING""")


def insert_albums():
    connection.execute("""INSERT INTO Album
    (album_name, artist_id, release_year)
    VALUES('Brilliant', 6, 2015)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, artist_id, release_year)
    VALUES('Changing winds', 7, 2009)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, artist_id, release_year)
    VALUES('2004', 8, 2019)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, artist_id, release_year)
    VALUES('All about whistles', 9, 2018)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, artist_id, release_year)
    VALUES('Beelive in Thunder', 10, 2018)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, artist_id, release_year)
    VALUES('In God we trust', 6, 2018)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, artist_id, release_year)
    VALUES('Stars', 12, 2017)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, artist_id, release_year)
    VALUES('Perfectness', 20, 2017)
    ON CONFLICT DO NOTHING""")


def insert_genres():
    engine.connect().execute("""INSERT INTO Genre
        (genre_name)
        VALUES('BritPop')
        ON CONFLICT DO NOTHING""")
    engine.connect().execute("""INSERT INTO Genre
        (genre_name)
        VALUES('Indie Rock')
        ON CONFLICT DO NOTHING""")
    engine.connect().execute("""INSERT INTO Genre
        (genre_name)
        VALUES('Rock')
        ON CONFLICT DO NOTHING""")
    engine.connect().execute("""INSERT INTO Genre
        (genre_name)
        VALUES('Syntpop')
        ON CONFLICT DO NOTHING""")
    engine.connect().execute("""INSERT INTO Genre
        (genre_name)
        VALUES('Pop')
        ON CONFLICT DO NOTHING""")


def insert_tracks():
    connection.execute("""INSERT INTO Track
        (track_name, duration, album_id, genre_id)
        VALUES('Organization', 173, 1, 2)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
            (track_name, duration, album_id, genre_id)
            VALUES('My life is brilliant', 201, 5, 3)
            ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                (track_name, duration, album_id, genre_id)
                VALUES('Bonfire hearts', 197, 5, 3)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                (track_name, duration, album_id, genre_id)
                VALUES('Wind of Change', 311, 6, 5)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                    (track_name, duration, album_id, genre_id)
                    VALUES('Maybe I Maybe You', 210, 6, 5)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                    (track_name, duration, album_id, genre_id)
                    VALUES('Кейс', 179, 7, 2)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                    (track_name, duration, album_id, genre_id)
                    VALUES('Положение', 362, 6, 5)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                    (track_name, duration, album_id, genre_id)
                    VALUES('Whistle', 224, 8, 6)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                        (track_name, duration, album_id, genre_id)
                        VALUES('Good feeling', 241, 8, 6)
                        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                        (track_name, duration, album_id, genre_id)
                        VALUES('Thunder', 187, 9, 4)
                        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                            (track_name, duration, album_id, genre_id)
                            VALUES('Natural', 189, 9, 4)
                            ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                            (track_name, duration, album_id, genre_id)
                            VALUES('Heathens', 195, 10, 4)
                            ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                            (track_name, duration, album_id, genre_id)
                            VALUES('Stressed Out', 222, 10, 7)
                            ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                            (track_name, duration, album_id, genre_id)
                            VALUES('Counting Stars', 257, 11, 7)
                            ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                                (track_name, duration, album_id, genre_id)
                                VALUES('Run', 157, 11, 7)
                                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                                (track_name, duration, album_id, genre_id)
                                VALUES('Perfect', 263, 12, 7)
                                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
                                (track_name, duration, album_id, genre_id)
                                VALUES('Shape of You', 263, 12, 7)
                                ON CONFLICT DO NOTHING""")


def insert_mixtapes():
    connection.execute("""INSERT INTO Mixtape
        (mixtape_name, release_year)
        VALUES(' Rap mixtape', 2017)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
            (mixtape_name, release_year)
            VALUES('Rocking music', 2019)
            ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Sheerans mix', 2018)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Pop mix', 2018)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Relax', 2010)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Motivation', 2021)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Dragons', 2019)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Exciting', 2019)
                ON CONFLICT DO NOTHING""")


def track_to_mix():
    connection.execute("""INSERT INTO TrackMixtape
                (track_id, mixtape_id)
                VALUES(14, 5)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(15, 10)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(25, 13)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(13, 14)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(26, 15)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(19, 16)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(20, 17)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(11, 18)
                    ON CONFLICT DO NOTHING""")


if __name__ == '__main__':
    insert_artist()
    insert_albums()
    insert_genres()
    insert_tracks()
    insert_mixtapes()
    track_to_mix()