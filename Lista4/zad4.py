# Author: Paweł Dychus
from inspect import getfullargspec
import math


class Norm:
    functions = []

    def __init__(self, f_to_add):
        # Remember the function by using class variable.
        Norm.functions.append(f_to_add)

    def __call__(self, *variables):
        for fun in Norm.functions:
            # If length of variables matches one's of the remembered functions, then call it with passed variables.
            if len(getfullargspec(fun).args) == len(variables):
                return fun(*variables)


def overload(func):
    return Norm(func)


@overload
def norm(x, y):
    return math.sqrt(x*x + y*y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2,4)}")
print(f"norm(2,3,4) = {norm(2,3,4)}")
