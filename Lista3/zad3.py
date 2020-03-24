def get_last_column(filename):
    with open(filename, 'r') as file_:
        return sum([int(line.split()[-1]) for line in file_])


print(get_last_column("test.txt"))
