"""Module which contains the dice support class."""
from random import randint


class Dice:
    """Class which contains the dice methods."""

    def __init__(self):
        """Initialises the face of the dice with 0."""
        self.face = 0

    def roll_dice(self):
        """Method which rolls the dice and prints the result."""

        self.face = randint(1, 6)

        faces = {1: "sides/one.txt",
                 2: "sides/two.txt",
                 3: "sides/three.txt",
                 4: "sides/four.txt",
                 5: "sides/five.txt",
                 6: "sides/six.txt"}

        with open(faces.get(self.face)) as side:
            print(side.read())

