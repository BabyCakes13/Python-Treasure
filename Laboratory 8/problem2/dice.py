"""
Module which contains the dice support class.
"""
from random import randint


class Dice:
    """Class which contains the dice methods."""

    def __init__(self):
        """
        Constructor of the Dice class.
        """
        self.face = 0

    def roll_dice(self):
        """
        Method which rolls the dice and prints the result.
        """

        self.face = randint(1, 6)

        faces = {1: "faces/one.txt",
                 2: "faces/two.txt",
                 3: "faces/three.txt",
                 4: "faces/four.txt",
                 5: "faces/five.txt",
                 6: "faces/six.txt"}

        with open(faces.get(self.face)) as side:
            print(side.read())

