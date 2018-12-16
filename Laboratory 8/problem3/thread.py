"""
Module which holds the CharThread.
"""
from threading import Lock, Thread


class CharThread(Thread):
    """
    Class which handles searching in a text for a character.
    """

    def __init__(self, character):
        """
        Constructor of the CharThread class.
        :param character: The desired character.
        """

        Thread.__init__(self)

        with open("text.txt", "r") as file:
            self.text = file.read()

        self.character = character

    def run(self):
        """
        Method which searches for a character in a text.
        """

        lock = Lock()

        with lock:
            counter = 0

            for char in self.text:
                if char == self.character:
                    counter += 1

            print("The character {0} appeared in the text {1} times".format(self.character, counter))
