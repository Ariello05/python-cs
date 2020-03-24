def all_subsets(list_):
    if list_ == []:
        return [[]]

    x, rest = list_[0], list_[1:]

    res = all_subsets(rest)
    res = list(map(lambda u: [x] + u, res)) + res
    return res


print(all_subsets([1, 2, 3]))
