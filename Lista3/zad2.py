def flatten(list_):
    iterator = iter(list_)
    iterStack = []

    while True:
        try:
            item = next(iterator)
            if isinstance(item, list):
                iterStack.append(iterator)
                iterator = iter(item)
            else:
                yield item
        except StopIteration:
            if len(iterStack) == 0:
                break
            else:
                iterator = iterStack.pop()


l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]
print(list(flatten(l)))
