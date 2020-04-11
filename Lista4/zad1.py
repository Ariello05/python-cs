# Author: Paweł Dychus
import time


def print_time(f):
    def timed_f(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("Elapsed time (s): {:.8f}".format(end-start))
        return result
    return timed_f


@print_time
def loopNtimes(n):
    sum = 0
    for i in range(n):
        sum += 1

    return sum


loopNtimes(10000000)
