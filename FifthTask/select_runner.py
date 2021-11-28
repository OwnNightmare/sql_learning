from selecting_module import *
import pandas as pd


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
        elif query == 'back':
            return 'main menu'
        elif query == 'h':
            print('\tСправка')
            print(helping)
        elif query in ['q', 'exit']:
            exit('Завершение сеанса')
        else:
            print('Unknown query. h - help')


def run_complex_select():
    query = ''
    helping = ("""
        \t\t\t'SQL запросы:  
        'aq' - 1) количество исполнителей в каждом жанре;
        'tq' - 2) количество треков, вошедших в альбомы 2019-2020 годов;
        'avg' - 3) средняя продолжительность треков по каждому альбому;
        'ex' - 4) все исполнители, которые не выпустили альбомы в 2020 году;
        'man' - 5) Сборники, где есть Maneskin;
        'fa' - 6) название альбомов, в которых присутствуют исполнители более 1 жанра;
        'nu' - 7) наименование треков, которые не входят в сборники
        'min' - 8) исполнителя, написавшего самый короткий по продолжительности трек;
        'sa' - 9) Самые "маленькие" альбомы;
        \t\t\tКоманды: 
        'h' - вызов данной справки;
        'q', 'exit' - выход
        """)
    print(helping)
    while query not in ['q', 'exit']:
        query = input('\t\nЗапрос или команда: ').lower().strip()
        if query == 'aq':
            print('Количество исполнителей по жанрам:')
            print(pd.DataFrame(count_artists_in_genre()))
        elif query == 'tq':
            print('Число треков из альбомов 2019-2020: ')
            print(pd.DataFrame(count_tracks_in_19_20(), columns='tracks number'))
        elif query == 'avg':
            print('Ср. продолжительность треков по альбомам: ')
            print(pd.DataFrame(find_avg_duration()))
        elif query == 'man':
            print('Сборники, где есть Maneskin: ')
            print(pd.DataFrame(get_mix_with_maneskin()))
        elif query == 'fa':
            print('Альбомы от артистов разных жанров: ')
            print(pd.DataFrame(get_feated_albums()))
        elif query == 'ex':
            print('Не выпускали альбомы в 2020: ')
            print(pd.DataFrame(get_not_in_2020()))
        elif query == 'nu':
            print('Этих треков нет в сборниках: ')
            print(pd.DataFrame(get_not_in_mixes()))
        elif query == 'min':
            print('Самые короткие треки и их исполнители: ')
            print(pd.DataFrame(get_shortest_tracks()))
        elif query == 'sa':
            print('Альбомы, с нимаеньшим числом треков: ')
            print(pd.DataFrame(get_shortest_albums()))
        elif query == 'back':
            return 'main menu'
        elif query == 'h':
            print('\tСправка')
            print(helping)
        elif query in ['q', 'exit']:
            exit('Завершение сеанса')
        else:
            print('Unknown query. h - help')


def run_main_menu():
    run = 'main menu'
    while run == 'main menu':
        print("""\tВыберите режим:\n'1' - запросы из одной таблицы;\n'2' - запросы из нескольких таблиц
('q' или 'exit' для выхода)""")
        mode = input('\tРежим: ')
        if mode == '1':
            run = run_simple_select()
        elif mode == '2':
            run = run_complex_select()
        elif mode in ['q', 'exit']:
            exit('Завершение сеанса')


if __name__ == '__main__':
    run_main_menu()
