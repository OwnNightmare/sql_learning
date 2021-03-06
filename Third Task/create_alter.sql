CREATE TABLE if NOT EXISTS Artist(
artist_id SERIAL,
artist_name VARCHAR(30) NOT NULL,
CONSTRAINT PK_Artist PRIMARY KEY(artist_id)
);

CREATE TABLE if NOT EXISTS Album(
album_id SERIAL,
album_name VARCHAR(40) NOT NULL,
release_year INTEGER,
CONSTRAINT PK_Album PRIMARY KEY (album_id)
);

CREATE TABLE if NOT EXISTS Artists_albums(
artist_id INTEGER,
album_id INTEGER,
CONSTRAINT PK_artist_album PRIMARY KEY(artist_id, album_id),
FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
FOREIGN KEY (album_id) REFERENCES Album(album_id)
);

CREATE TABLE if NOT EXISTS Genre(
genre_id SERIAL,
genre_name VARCHAR(40) NOT NULL,
CONSTRAINT PK_genre PRIMARY KEY(genre_id)
);

CREATE TABLE if NOT EXISTS Artists_genre(
artist_id INTEGER,
genre_id INTEGER,
CONSTRAINT PK_artists_genre PRIMARY KEY(artist_id, genre_id)
FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE if NOT EXISTS Track(
track_id SERIAL,
track_name VARCHAR(40) NOT NULL,
duration INTEGER,
album_id INTEGER,
CONSTRAINT PK_Track PRIMARY KEY (track_id),
CONSTRAINT unique_track UNIQUE(track_name),
FOREIGN KEY (album_id) REFERENCES Album (album_id)
);


CREATE TABLE if NOT EXISTS Mixtape(
mixtape_id SERIAL,
mixtape_name VARCHAR(30) NOT NULL,
CONSTRAINT PK_mixtape PRIMARY KEY(mixtape_id),
CONSTRAINT unique_mix UNIQUE(mixtape_name)
);

CREATE TABLE if NOT EXISTS TrackMixtape(
track_id INTEGER,
mixtape_id INTEGER,
CONSTRAINT track_and_mixtape_ids PRIMARY KEY(track_id, mixtape_id),
FOREIGN KEY (track_id) REFERENCES track(track_id),
FOREIGN KEY (mixtape_id) REFERENCES Mixtape(mixtape_id)
 );

ALTER TABLE Mixtape
ADD COLUMN release_year INTEGER;

ALTER TABLE Artist
ADD CONSTRAINT unique_artist UNIQUE(artist_name);

ALTER TABLE Genre
ADD CONSTRAINT unique_genre UNIQUE(genre_name);

ALTER TABLE Album
ADD CONSTRAINT unique_album UNIQUE(album_name);



