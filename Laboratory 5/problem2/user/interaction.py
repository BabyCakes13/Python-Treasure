"""Module which handles user input and calls the functions for area computation."""
from problem2.user import strings as s
from problem2 import Shape


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
               3: triangle_handler,
               4: circle_handler}

    strings = {1: s.square_strings(),
               2: s.rectangle_strings(),
               3: s.triangle_strings(),
               4: s.circle_strings()}

    valid = options.get(option, error_handler)
    if valid == error_handler:
        valid()
        return
    valid(strings.get(option, error_handler))


def square_handler(string):
    """Method which computes the square area."""

    a = int(input(string[0]))

    square = Shape.Square(a)

    print(string[1] + square.display() + " is " + str(square.getarea()))


def rectangle_handler(string):
    """Method which computes the rectangle area."""

    a = int(input(string[0]))
    b = int(input(string[1]))

    rectangle = Shape.Rectangle(a, b)

    print(string[2] + rectangle.display() + " is " + str(rectangle.getarea()))


def triangle_handler(string):
    """Method which computes the triangle area."""

    a = int(input(string[0]))
    b = int(input(string[1]))
    c = int(input(string[2]))

    triangle = Shape.Triangle(a, b, c)

    print(string[3] + triangle.display() + " is " + str(round(triangle.getarea(), 2)))


def circle_handler(string):
    """Method which computes the circle area."""

    r = int(input(string[0]))

    circle = Shape.Circle(r)

    print(string[1] + circle.display() + " is " + str(round(circle.getarea(), 2)))


def error_handler():
    print("Invalid option, please try again")

