"""
Module which uses the Char Thread. Not such a nice thread.
"""
from problem3 import thread


if __name__ == "__main__":

    letters = ['a', 'e', 'x', 'w', 'g']

    for letter in letters:
        t = thread.CharThread(letter)
        t.start()
