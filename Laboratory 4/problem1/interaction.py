"""Module which handles user input and calls the functions for area computation."""
from problem1.util import strings as s
from problem1 import shapes


def initiate():
    """Method which takes the option from the user and computes the selected area."""

    option = 0

    try:
        option = int(input(s.main_question()))
    except ValueError:
        print("Wrong input.\n")
        exit(-1)

    options = {1: square_handler,
               2: rectangle_handler,
               3: triangle_handler}

    strings = {1: s.square_strings(),
               2: s.rectangle_strings(),
               3: s.triangle_strings()}

    valid = options.get(option, error_handler)
    if valid == error_handler:
        valid()
        return
    valid(strings.get(option, error_handler))


def square_handler(string):
    """Method which computes the square area."""

    a = int(input(string[0]))

    print(string[1] + str(shapes.square_area(a)))


def rectangle_handler(string):
    """Method which computes the rectangle area."""

    a = int(input(string[0]))
    b = int(input(string[1]))

    print(string[2] + str(shapes.rectangle_area(a, b)))


def triangle_handler(string):
    """Method which computes the triangle area."""

    a = int(input(string[0]))
    b = int(input(string[1]))
    c = int(input(string[2]))

    print(string[3] + str(round(shapes.triangle_area(a, b, c), 3)))


def error_handler():
    print("Invalid option, please try again")
