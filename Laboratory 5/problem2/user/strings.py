"""Module which contains the strings used in the application."""


def main_question():
    """Contains the text to be displayed to console for the first question."""

    return "Enter the shape for which you want to compute the area:\n" \
           " 1. Square\n" \
           " 2. Rectangle\n" \
           " 3. Triangle\n" \
           " 4. Circle\n"


def circle_strings():
    """Contains the text to be displayed to console for the option 1."""

    strings = ["Enter the radius of the circle:\n",
               "The area of the "]

    return strings


def square_strings():
    """Contains the text to be displayed to console for the option 1."""

    strings = ["Enter the side of the square:\n",
               "The area of the "]

    return strings


def rectangle_strings():
    """Contains the text to be displayed to console for the option 2."""

    strings = ["Enter the first side of the rectangle:\n",
               "Enter the second side of the rectangle:\n",
               "The area of the "]

    return strings


def triangle_strings():
    """Contains the text to be displayed to console for the option 3."""

    strings = ["Enter the first side of the triangle:\n",
               "Enter the second side of the triangle:\n",
               "Enter the third side of the triangle:\n",
               "The area of the "]

    return strings
