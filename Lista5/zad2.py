# autor Dychus Paweł
import numpy as np
import os
import sys
from colors import *


def reached_m(value, m):
    return value >= m + 1


def truncate_data(f, valid_userID):
    while True:
        line = f.readline()
        if not line:
            return
        userID, _, _, _ = line.split(',')

        if userID != valid_userID:
            now = f.tell()
            f.seek(now - len(line) - 1, os.SEEK_SET)
            return


def read_data(firstline, f, m, allowed_ids):
    valid_userID, movieID, rating, _ = firstline.split(',')
    movieID = int(movieID)
    rating = float(rating)

    result = {}
    for el in allowed_ids:
        result[el] = 0

    while True:

        if movieID > m:
            truncate_data(f, valid_userID)
            break

        result[movieID] = rating
        line = f.readline()
        if not line:
            break

        userID, movieID, rating, _ = line.split(',')
        if userID != valid_userID:
            now = f.tell()
            f.seek(now - len(line) - 1, os.SEEK_SET)
            break

        movieID = int(movieID)
        rating = float(rating)

    return result


def get_data():
    print("Reading film ids")
    film_ids = get_film_ids(10000)
    print(f"Read: {len(film_ids)} ids")
    print("Reading user data")
    allowed_ids = []
    for keys in film_ids.keys():
        allowed_ids.append(keys)

    with open('ratings.csv', "r") as f:
        line = f.readline()  # ignore first line
        result = []
        line = f.readline()
        count = 1
        while line:
            dict_ = read_data(line, f, 10000, allowed_ids)
            result.append(dict_)

            if len(dict_) != len(film_ids):
                raise AssertionError("Assert! - list can't have length != m")

            line = f.readline()
            if len(result) % 100 == 0:
                print(f"Read up to: \t{100 * count} users...")
                count += 1

        print(f'Read total of:\t {len(result)} users.')
        print(f"Matrix of size: {len(result)}x{len(film_ids)}")
        return result, film_ids


def get_film_ids(m):
    with open('movies.csv', "r", encoding='utf-8') as f:
        line = f.readline()  # ignore first line
        names = {}
        line = f.readline()
        while line:
            data = line.split(',')
            id = int(data[0])
            if id > m:
                break

            name = ','.join(data[1:len(data) - 1])
            names[id] = name
            line = f.readline()

        return names


def normalize_data(x):
    list_ = []
    for dict_ in x:
        row = []
        for values in dict_.values():
            row.append(values)

        list_.append(row)

    list_ = np.array(list_)
    normalized = list_ / np.linalg.norm(list_, axis=0)  # znormalizowana macierz
    np.nan_to_num(normalized, copy=False)
    return normalized


def setup_ratings(film_ids, user_ratings):
    my_ratings = {}
    # dictionary because we don't allow non existent films i.e:
    # 32,Twelve Monkeys (a.k.a. 12 Monkeys) (1995),Mystery|Sci-Fi|Thriller
    # 34,Babe (1995),Children|Drama
    # Notice lack of number 33

    for key in film_ids.keys():
        my_ratings[key] = 0

    if user_ratings is None:
        print(
            "Assuming ratings:\n my_ratings[2571] = 5\n my_ratings[32] = 4\n my_ratings[260] = 5\n my_ratings[1097] = 4\n")
        my_ratings[2571] = 5  # patrz movies.csv  2571 - Matrix
        my_ratings[32] = 4  # 32 - Twelve Monkeys
        my_ratings[260] = 5  # 260 - Star Wars IV
        my_ratings[1097] = 4
    else:
        for item,key in user_ratings.items():
            if key > len(film_ids):
                raise Exception(f"Key of value ({key}) not allowed!")
            my_ratings[key] = item

    list_ = []  # back to 0..m notion
    for el in my_ratings.values():
        list_.append([el])

    return np.array(list_)


def process_ratings(my_ratings, normalized, film_names):
    # obliczamy podobieństwo cosinusowe z każdym użytkownikiem (skorzystamy z mnożenia macierzowego)
    z = np.dot(normalized, np.array(my_ratings) / np.linalg.norm(my_ratings))
    # normalizujemy otrzymany wektor (będzie on reprezentował nasz profil filmowy)
    z = z / np.linalg.norm(z)
    final = np.dot(normalized.T, z)

    rating_name_pairs = []
    i = 0
    for keys in film_names.keys():
        rating_name_pairs.append((final[i][0], film_names[keys]))
        i += 1

    # for i in range(0, len(film_names)):
    #    rating_name_pairs.append((final[i][0], film_names[i]))

    return rating_name_pairs


def print_results(rating_name_pairs):
    rating_name_pairs = sorted(rating_name_pairs, key=lambda u: u[0], reverse=True)
    amount = int(input("How many top records to print\n> "))

    for i in range(amount):
        print(rating_name_pairs[i])

def standard(user_ratings = None):
    result, film_ids = get_data()
    normalized = normalize_data(result)
    my_ratings = setup_ratings(film_ids, user_ratings)
    rating_name_pairs = process_ratings(my_ratings, normalized, film_ids)
    print_results(rating_name_pairs)

if __name__ == "__main__":


    try:
        if len(sys.argv) < 2:
            raise Exception(f"Expected: {OPENBLUE}-t number | -s {CLOSECOLOR}\n Got:\t  {' '.join(sys.argv[1:])}")
        elif len(sys.argv) == 2:
            token = sys.argv[1]
            print(token)
            if token != '-s':
                raise Exception(f"Expected: {OPENBLUE}-t number | -s {CLOSECOLOR}\n Got:\t  {' '.join(sys.argv[1:])}")

            standard()
            print(f"{OPENGREEN}SUCCESS{CLOSECOLOR}")
        elif len(sys.argv) == 3:
            param = sys.argv[1]
            if param != '-t':
                raise Exception(f"Expected: {OPENBLUE}-t number | -s {CLOSECOLOR}\n Got:\t  {' '.join(sys.argv[1:])}")
            number = int(sys.argv[2])
            print("Write pairs: id rating")
            dict_ = {}
            for i in range(number):
                str_ = input("> ")
                splitted = str_.split(' ')
                try:
                    id = int(splitted[0])
                    rating = int(splitted[1])
                    dict_[id] = rating
                except Exception:
                    print(f"Expected: {OPENBLUE}id rating{CLOSECOLOR}\n Got:\t  {str_}")
                    print("Try again...")
                    continue

            standard(dict_)

    except Exception as e:
        print(e)
        print(f"{OPENRED}FAILURE{CLOSECOLOR}")

