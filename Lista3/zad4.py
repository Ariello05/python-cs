
def qs(list_):
    if len(list_) == 0 or len(list_) == 1:
        return list_

    x, rest = list_[0], list_[1:]

    return qs(list(filter(lambda u: u <= x, rest))) + [x] + qs(list(filter(lambda u: u > x, rest)))


print(qs([2, 1, 1, 3, 3, 3, 4, 5, 6, 1, 0, -1]))
