CREATE TABLE if NOT EXISTS performer(
id serial PRIMARY KEY,
performer_name VARCHAR(30) NOT NULL
);

CREATE TABLE if NOT EXISTS album(
id serial PRIMARY KEY,
album_name VARCHAR(40) NOT NULL,
release_year DATE,
performer_id INTEGER REFERENCES performer(id)
);

CREATE TABLE if NOT EXISTS track(
id serial PRIMARY KEY,
track_name VARCHAR(25) NOT NULL,
duration INTEGER,
album_id INTEGER REFERENCES album(id)
);

CREATE TABLE if NOT EXISTS genre(
genre_name VARCHAR(20) PRIMARY KEY
);

ALTER TABLE performer
ADD COLUMN genre VARCHAR(20) REFERENCES genre(genre_name)
;