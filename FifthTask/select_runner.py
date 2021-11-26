from selecting_module import *


def run_simple_select():
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
        query = input('\tЗапрос или команда: ').lower().strip()
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


def run_complex_query():
    query = ''
    helping = ("""
        \t\t\t'SQL запросы:  
        'aq' - количество исполнителей в каждом жанре;
        'tq' - количество треков, вошедших в альбомы 2019-2020 годов;
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
        query = input('\tЗапрос или команда: ').lower().strip()
        if query == 'aq':
            print('Количество исполнителей по жанрам:')
            count_artists_in_genre()
        elif query == 'tq':
            print('Число треков из альбомов 2019-2020: ')
            count_tracks_in_19_20()
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


run_complex_query()