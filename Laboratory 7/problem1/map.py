"""
Module which contains functions for converting fahrenheit to celsius.
"""
import util


def convert_celsius():
    """
        Method to convert celsius to fahrenheit.

        Takes a list of numbers representing celsius temperatures and uses lambda expression
        to map the fahrenheit converting formula to the celsius list.

        :return: a list of fahrenheit degrees representing the converted celsius numbers.
        """

    celsius = [6, 11, 9.5, 15, 22, 27, 24, 30.3, 37.5, 44]
    fahrenheit = map(lambda c: round((9 / 5) * c + 32, 2), celsius)

    return fahrenheit


def convert_fahrenheit():
    """
    Method to convert fahrenheit to celsius.

    Takes a list of numbers representing fahrenheit temperatures and uses lambda expression
    to map the celsius converting formula to the fahrenheit list.

    :return: a list of celsius degrees representing the converted fahrenheit numbers.
    """
    fahrenheit = [37, 29, 40, 58.6, 20, 68, 21.5, 0, 77, 34]
    celsius = map(lambda f: round((5 / 9) * (f - 32), 2), fahrenheit)

    return celsius


if __name__ == "__main__":

    print("\nCELSIUS TO FAHRENHEIT: \n")
    util.pretty_print(convert_celsius())

    print("\n\nFAHRENHEIT TO CELSIUS: \n")
    util.pretty_print(convert_fahrenheit())
