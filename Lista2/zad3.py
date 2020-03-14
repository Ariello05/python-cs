from os import rename, walk


def walkDirs(dirname):
    for (dirpath, dirnames, filenames) in walk(dirname):
        for file_ in filenames:
            new_ = file_.lower()
            rename(dirpath+"/"+file_, dirpath+"/"+new_)

        for dir_ in dirnames:
            new_ = dir_.lower()
            rename(dirpath+"/"+dir_, dirpath+"/"+new_)


walkDirs("./testfolder")
