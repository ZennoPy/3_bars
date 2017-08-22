import json
import sys


def load_json_data(filepath):
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(json_data):
    return max(json_data, key=lambda bars:bars['SeatsCount'])['Name']


def get_smallest_bar(json_data):
    return min(json_data, key=lambda bars: bars['SeatsCount'])['Name']


def get_closest_bar(json_data, longitude, latitude):
    pass


if __name__ == '__main__':
    try:
        if not len(sys.argv) > 1:
            filepath = input("Укажите путь к файлу: ")
            sys.exit()
        json_content = load_json_data(sys.argv[1])
        print("Самый большой бар - " + get_biggest_bar(json_content))
        print("Самый маленький бар - " + get_smallest_bar(json_content))
    except IndexError:
        print("Do not specify the path to the file")
    except FileNotFoundError:
        print("The specified file was not found")
