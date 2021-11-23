import sqlalchemy
from sqlalchemy import *
metadata = MetaData()

db = 'postgresql://me:password@localhost:5432/my_db'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


def insert_artist():
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('Maneskin')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('Oxxxymiron')
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Artist(artist_name)
    VALUES('Scorpions')
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
    (album_name, release_year)
    VALUES('Teatro d`ira - Vol. I', 2021)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, release_year)
    VALUES('ГорГород', 2015)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
    (album_name, release_year)
    VALUES('Born to touch your feelings', 2017)
    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
        (album_name, release_year)
        VALUES('In my mind Part 3', 2018)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
        (album_name, release_year)
        VALUES('Origins', 2018)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
        (album_name, release_year)
        VALUES('Trench', 2018)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
        (album_name, release_year)
        VALUES('Human', 2021)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Album
        (album_name, release_year)
        VALUES('=', 2018)
        ON CONFLICT DO NOTHING""")


def create_artists_and_albums():
    artist = Table('Artist_', metadata,
            Column('artist_id', Integer, autoincrement=True, primary_key=True),
            Column('artist_name', String(40), unique=False)
                   )

    album = Table('Albums', metadata,
           Column('album_id', Integer, autoincrement=True, primary_key=True),
           Column('album_name', String(40), unique=False),
           Column('release_year', Integer)
                  )

    artists_albums = Table('artists_albums', metadata,
            Column('artist_id', Integer, ForeignKey('Artist_.artist_id'), primary_key=True),
            Column('album_id', Integer, ForeignKey('Albums.album_id'), primary_key=True)
    )
    metadata.create_all(engine)

    def insertion_alchemy():
        try:
            art_names = (['Maneskin', 'Oxxxymiron', 'Scorpions', 'Fio Rida', 'Imagine Dragons',
                         'Twenty one pistols', 'OneRepublic', 'Ed Sheeran'])
            alb_names = [('Teatro d`ira - Vol. I', 2021), ('ГорГород', 2015),
                         ('Born to touch your feelings', 2017),
                         ('In my mind Part 3', 2018), ('Origins', 2018),
                         ('Trench', 2018), ('Human', 2021), ('=', 2018)
                         ]
            print(len(alb_names) == len(art_names))
            for art_name in art_names:
                ins = artist.insert().values(artist_name=art_name)
                connection.execute(ins)
            for alb_name in alb_names:
                name, year = alb_name
                ins_al = album.insert().values(album_name=name, release_year=year)
                connection.execute(ins_al)
        finally:
            if len(alb_names) == len(art_names):
                ar_id = 1
                al_id = 1
                for i in range(len(art_names)):
                    ins = artists_albums.insert().values(artist_id=ar_id, album_id=al_id)
                    connection.execute(ins)
                    ar_id += 1
                    al_id += 1
    insertion_alchemy()


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
        (track_name, duration, album_id)
        VALUES('Begging', 211, 1)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
        (track_name, duration, album_id)
        VALUES('ZITTI E BUONI', 211, 1)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
        (track_name, duration, album_id)
        VALUES('Город под подошвой', 246, 2)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
        (track_name, duration, album_id)
        VALUES('Переплетено', 291, 2)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
        (track_name, duration, album_id)
        VALUES('WInd of change', 311, 3)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
        (track_name, duration, album_id)
         VALUES('Humanity', 326, 3)
         ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
         (track_name, duration, album_id)
         VALUES('Whistle', 224, 4)
         ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
         (track_name, duration, album_id)
         VALUES('Low', 230, 4)
          ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
          (track_name, duration, album_id)
          VALUES('Natural', 189, 5)
          ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
          (track_name, duration, album_id)
          VALUES('Thunder', 187, 5)
          ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
          (track_name, duration, album_id)
          VALUES('Stressed Out', 202, 6)
          ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
          (track_name, duration, album_id)
           VALUES('Heathens', 195, 6)
           ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
           (track_name, duration, album_id)
           VALUES('Counting Stars', 257, 7)
           ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
           (track_name, duration, album_id)
           VALUES('Apologize', 183, 7)
           ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
           (track_name, duration, album_id)
           VALUES('Perfect', 263, 8)
           ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Track
           (track_name, duration, album_id)
           VALUES('Beautiful people', 197, 8)
           ON CONFLICT DO NOTHING""")


def insert_mixtapes():
    connection.execute("""INSERT INTO Mixtape
        (mixtape_name, release_year)
        VALUES('Rock mixtape', 2017)
        ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
            (mixtape_name, release_year)
            VALUES('Pop mixtape', 2019)
            ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Dark times', 2018)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Relaxing', 2020)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO Mixtape
                (mixtape_name, release_year)
                VALUES('Training', 2010)
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
                VALUES(1, 1)
                ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(2, 2)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(3, 3)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(4, 3)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(1, 4)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(1, 5)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(7, 6)
                    ON CONFLICT DO NOTHING""")
    connection.execute("""INSERT INTO TrackMixtape
                    (track_id, mixtape_id)
                    VALUES(8, 8)
                    ON CONFLICT DO NOTHING""")


def using_alchemy():
    u = 'user_name'
    user = Table('user', metadata,
        Column('user_id', Integer, autoincrement=True, primary_key=True),
        Column(u, String(30))
                 )
    metadata.create_all(engine)


if __name__ == '__main__':
    insert_artist()
    insert_albums()
    insert_tracks()
    insert_mixtapes()
    track_to_mix()
    create_artists_and_albums()