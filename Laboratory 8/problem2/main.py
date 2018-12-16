"""
Module which tests the dice thread. This is even a better thread.
"""
from problem2 import thread
import IO


if __name__ == "__main__":

    number = IO.get_number()

    for i in range(number):
        t = thread.ThreadDice(name="Thread-" + str(i))
        t.start()
