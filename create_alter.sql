CREATE TABLE if NOT EXISTS Artist(
artist_id SERIAL,
artist_name VARCHAR(30) NOT NULL,
CONSTRAINT PK_Artist PRIMARY KEY(artist_id)
);

CREATE TABLE if NOT EXISTS Album(
album_id SERIAL,
album_name VARCHAR(40) NOT NULL,
artist_id INTEGER NOT NULL,
release_year INTEGER,
CONSTRAINT PK_Album PRIMARY KEY (album_id),
FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

CREATE TABLE if NOT EXISTS Genre(
genre_id SERIAL,
genre_name VARCHAR(40) NOT NULL,
CONSTRAINT PK_genre PRIMARY KEY(genre_id)
);

CREATE TABLE if NOT EXISTS Track(
track_id SERIAL,
track_name VARCHAR(40) NOT NULL,
duration INTEGER,
album_id INTEGER,
genre_id INTEGER,
CONSTRAINT PK_Track PRIMARY KEY (track_id),
FOREIGN KEY (album_id) REFERENCES Album (album_id),
FOREIGN KEY (genre_id) REFERENCES Genre (genre_id)
);

ALTER TABLE track
ADD CONSTRAINT unique_track UNIQUE(track_name);

CREATE TABLE if NOT EXISTS Mixtape(
mixtape_id SERIAL,
mixtape_name VARCHAR(30) NOT NULL,
CONSTRAINT PK_mixtape PRIMARY KEY(mixtape_id)
);

 CREATE TABLE if NOT EXISTS TrackMixtape(
 track_id INTEGER,
 mixtape_id INTEGER,
 CONSTRAINT track_and_mixtape_ids PRIMARY KEY(track_id, mixtape_id),
 FOREIGN KEY (track_id) REFERENCES track(track_id),
 FOREIGN KEY (mixtape_id) REFERENCES Mixtape(mixtape_id)
 );

ALTER TABLE Mixtape
ADD CONSTRAINT unique_mix UNIQUE(mixtape_name);

ALTER TABLE Mixtape
ADD COLUMN release_year INTEGER;

ALTER TABLE Artist
ADD CONSTRAINT unique_artist UNIQUE(artist_name);

INSERT INTO Artist(artist_name)
VALUES('Oxxxymiron')
ON CONFLICT DO NOTHING;

INSERT INTO Track(track_name, duration)
VALUES('Moh', 175)
ON CONFLICT DO NOTHING;

INSERT INTO Genre(genre_name)
VALUES('Hip-hop')
ON CONFLICT DO NOTHING;

INSERT INTO Album
VALUES(1, 'Dark Time', 1, 2021)
ON CONFLICT DO NOTHING;

UPDATE Track
    SET album_id = 1, genre_id = 2
    WHERE track_id = 8;

 INSERT INTO Mixtape(mixtape_name)
 VALUES('Moh is all around us')
 ON CONFLICT DO NOTHING;

 UPDATE Mixtapes
    SET release_year = 2020
    WHERE mixtape_id = 2;

 INSERT INTO TrackMixtape
 VALUES(8,2)
 ON CONFLICT DO NOTHING;

 ALTER TABLE Genre
 ADD CONSTRAINT unique_genre UNIQUE(genre_name);

 ALTER TABLE Album
 ADD CONSTRAINT unique_album UNIQUE(album_name);
