from os import rename, walk
from colors import *
import sys


def walk_dirs(dirname):
    for (dirpath, dirnames, filenames) in walk(dirname):
        for file_ in filenames:
            new_ = file_.lower()
            rename(dirpath+"/"+file_, dirpath+"/"+new_)

        for dir_ in dirnames:
            new_ = dir_.lower()
            rename(dirpath+"/"+dir_, dirpath+"/"+new_)


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
            walk_dirs(filepath)
            print(f"{OPENGREEN}SUCCESS{CLOSECOLOR}")
    except:
        print(f"{OPENRED}FAILURE{CLOSECOLOR}")
        raise
