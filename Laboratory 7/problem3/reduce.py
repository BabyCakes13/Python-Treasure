"""
Module which contains reduce() examples.
"""
import functools as f


def get_max():
    """
    Method which find the maximum value from the list using lambda expressions.
    :return: An integer representing the maximum value from the list.
    """

    values = [12, 32, 1, 73, 25, 68, 83, 29, 55, 61, 100, 97, 2]

    return f.reduce(lambda x, y: x if (x > y) else y, values)


if __name__ == "__main__":

    print("MAXIMUM: ")
    print(get_max())
