import hashlib
from os import rename, walk, path
from colors import *
import sys

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


def get_file_hash(filepath):
    md5 = hashlib.md5()

    with open(filepath, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)

    return md5.hexdigest()


def find_same(dirname):
    hash_dictionary = {}

    for (dirpath, _, filenames) in walk(dirname):
        for file_ in filenames:

            path_ = dirpath+"\\"+file_
            file_size = path.getsize(path_)
            hash_code = get_file_hash(path_)

            if (file_size, hash_code) not in hash_dictionary:
                hash_dictionary[(file_size, hash_code)] = [path_]
            else:
                hash_dictionary[(file_size, hash_code)].append(path_)

    for list_ in hash_dictionary.values():
        if len(list_) > 1:
            max_ = 0
            for path_ in list_:
                print(f"{OPENGREEN}{path_}{CLOSECOLOR}")
                if len(path_) > max_:
                    max_ = len(path_)

            print("-"*max_)


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print(f"{OPENRED}FAILURE{CLOSECOLOR}")
            print(
                f"Expected: {OPENBLUE}filepath{CLOSECOLOR}")
            print(
                f"Got:\t  {' '.join(sys.argv[1:])}")
        else:
            filepath = sys.argv[1]
            find_same(filepath)
            print(f"{OPENGREEN}SUCCESS{CLOSECOLOR}")
    except:
        print(f"{OPENRED}FAILURE{CLOSECOLOR}")
        raise
