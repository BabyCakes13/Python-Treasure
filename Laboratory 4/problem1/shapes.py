"""Module which contains shape area computation functions."""


def square_area(a):
    """Method which returns the area of a square."""
    return a*a


def rectangle_area(a, b):
    """Method which returns the area of a rectangle."""
    return a*b


def triangle_area(a, b, c):
    """Method which returns the area of a triangle."""

    if is_triangle([a, b, c]) is True:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    else:
        print("The triangle is not valid.")
        exit(-1)


def is_triangle(sides):
    """Checks whether the triangle is a valid one."""

    smallest, medium, biggest = sorted(sides)

    return smallest + medium > biggest and all(s > 0 for s in sides)
