"""
Module which handles user input operations.
"""


def get_number():
    """
    Method which asks the user to give a valid number.
    :return: The given number.
    """

    while True:
        try:
            number = int(input("Give the number: "))
            if number < 1:
                print('The number must not be less than or equal to 0. Try again :)')
                continue
            break
        except ValueError:
            print("The number must be an integer.")
            continue

    return number
