"""
Module which handles user input operations.
"""
from queue import Queue


def get_number():
    """
    Method which asks the user to give a valid number of lists to be sorted.
    :return: The number of lists to be sorted.
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


def get_queue(number):
    """
    Method which asks the user for the lists and creates a queue formed of them.
    :param number: The number of lists.
    :return: The queue formed of all lists.
    """
    queue = Queue()

    for i in range(number):
        baby_list = [int(x) for x in input("Give a list: ").split()]
        queue.put(baby_list)

    return queue
