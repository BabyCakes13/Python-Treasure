"""
Module which holds the ThreadDice class. For people who really like dices.
"""
from threading import Thread
from problem2 import dice


class ThreadDice(Thread):
    """
    Thread which rolls a dice.
    """

    def __init__(self, name):
        """
        Constructor of the dice thread.
        """

        Thread.__init__(self)
        self.name = name
        self.dice = dice.Dice()

    def run(self):
        """
        Method which rolls and prints the dice.
        """

        print(self.name + " has started...")
        self.dice.roll_dice()
        print(self.name + " has rolled " + str(self.dice.face) + ".")
