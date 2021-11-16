create table if not exists performer(
id serial primary key,
performer_name varchar(30) not null
);

create table if not exists album(
id serial primary key,
album_name varchar(20) not null,
release_year integer,
performer_id integer references performer(id)
);

create table if not exists track(
id serial primary key,
track_name varchar(40) not null,
duration interval,
performer_id integer references performer(id),
album_id integer references album(id)
);