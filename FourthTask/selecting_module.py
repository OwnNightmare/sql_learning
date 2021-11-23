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


def run_display():
    query = ''
    helping = ("""
    \t\t\t'SQL запросы:  
    'al' - название и год выхода альбомов, вышедших в 2018 году;
    'lt' - название и продолжительность самого длительного трека;
    'lts' - название треков, продолжительность которых не менее 3,5 минуты;
    'mx' - названия сборников, вышедших в период с 2018 по 2020 год включительно;
    'art' - исполнители, чье имя состоит из 1 слова;
    'my' - название треков, которые содержат слово "мой"/"my" ;
    \t\t\tКоманды: 
    'h' - вызов данной справки;
    'q', 'exit' - выход
    """)
    print(helping)
    while query not in ['q', 'exit']:
        query = input('\tЗапрос или команда: ').lower()
        if query == 'al':
            print('Альбомы, вышедшие в 2018:')
            get_albums()
        elif query == 'lt':
            print('Самый продолжительный трек: ')
            get_longest()
        elif query == 'lts':
            print('Треки не менее 3.5 минут: ')
            get_long_tracks()
        elif query == 'mx':
            print('Сборники 2018 - 2020: ')
            get_mix_in_18_20()
        elif query == 'art':
            print('Имена артистов из 1 слова: ')
            get_one_worded()
        elif query == 'my':
            print('Трек содержит слово my/мой')
            get_with_my()
        elif query == 'h':
            print('\tСправка')
            print(helping)
        elif query in ['q', 'exit']:
            exit('Завершение сеанса')
        else:
            print('Unknown query. h - help')


run_display()
