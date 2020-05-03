#autor Dychus Paweł
import numpy as np
import matplotlib.pyplot as plt
import os


def reached_m(value, m):
    return value >= m + 2


def read_data(valid_userID, f, m):
    line = f.readline()
    userID, movieID, rating, _ = line.split(',')
    movieID = int(movieID)
    rating = float(rating)
    film_counter = 2

    while True:

        if movieID != film_counter:
            for i in range(film_counter, movieID):
                if reached_m(i, m):
                    return
                yield 0.0

        if reached_m(movieID, m):
            return

        yield float(rating)

        line = f.readline()
        if not line:
            return
        film_counter = movieID + 1

        userID, movieID, rating, _ = line.split(',')
        if userID != valid_userID:
            if film_counter < m:
                for i in range(film_counter, m + 2):
                    yield 0.0
            now = f.tell()
            f.seek(now - len(line), os.SEEK_SET)
            return

        movieID = int(movieID)
        rating = float(rating)


def get_data(m):
    with open('ratings.csv', "r") as f:
        line = f.readline()  # ignore first line
        y = []
        x = []

        line = f.readline()
        while line:
            userID, movieID, rating, _ = line.split(',')

            if int(movieID) == 1:
                y.append(float(rating))
                list_ = list(read_data(userID, f, m))
                x.append(list_)
                if len(list_) != m:
                    raise RuntimeError("Assert! - list can't have length != m")
            line = f.readline()

        return (x, y)


def get_prediction(x, y, prediction_x):
    x = np.array(x)
    y = np.array(y)
    prediction_x = np.array(prediction_x)

    solved = np.linalg.lstsq(x, y, rcond=None)[0]
    predictions = []

    for line in prediction_x:
        sum_ = 0
        for i in range(len(solved)):
            sum_ += line[i] * solved[i]
        predictions.append(sum_)

    return np.array(predictions)


def load_predict(m, test=False):
    print(f"Loading data for m={m}")
    x, y = get_data(m)
    if test:
        y_pred = get_prediction(x[:200], y[:200], x[200:])
    else:
        y_pred = get_prediction(x, y, x)

    return y_pred


def save_as_plt(range_, prediction, true, m):
    plt.plot(range_, prediction, 'o', label="predicted", color="r", markersize=3)
    plt.plot(range_, true[200:], 'o', label="true", color="g", markersize=2)
    plt.title(f"Prediction to true value comparison for m={m}")
    plt.legend()
    plt.savefig(f'm{m}')
    plt.close()


def task1():
    _, y = get_data(1)  # get y
    y_10 = load_predict(10)
    errors10 = (abs(y_10 - y))
    y_1000 = load_predict(1000)
    errors1000 = (abs(y_1000 - y))
    y_10000 = load_predict(10000)
    errors10000 = (abs(y_10000 - y))

    print(f"Finished loading, showing the charts")

    r = range(215)
    plt.plot(r, errors10, 'o', label="m=10", color="r", markersize=1)
    plt.plot(r, errors1000, 'o', label="m=1000", color="g", markersize=3)
    plt.plot(r, errors10000, 'o', label="m=10000", color="b", markersize=2)
    plt.title("Errors: |prediction-true|")
    plt.legend()
    plt.show()


def task2():
    _, y = get_data(1)  # get y
    y_pred10 = load_predict(10, True)
    y_pred100 = load_predict(100, True)
    y_pred200 = load_predict(200, True)
    y_pred500 = load_predict(500, True)
    y_pred1000 = load_predict(1000, True)
    y_pred10000 = load_predict(10000, True)

    print(f"Finished loading, saving the predictions into: "
          f"m<x>.png")
    r = range(15)

    save_as_plt(r, y_pred10, y, 10)
    save_as_plt(r, y_pred100, y, 100)
    save_as_plt(r, y_pred200, y, 200)
    save_as_plt(r, y_pred500, y, 500)
    save_as_plt(r, y_pred1000, y, 1000)
    save_as_plt(r, y_pred10000, y, 10000)


if __name__ == "__main__":
    got = input(
        "Press:\n [1] for subtask 1 (regresja liniowa na całym zbiorze)\n [2] for subtask 2 (regresja liniowa ze zbiorem testowym)\n> ")
    if got == "1":
        task1()
    elif got == '2':
        task2()
    else:
        print("Unkown symbol, try again ...")
