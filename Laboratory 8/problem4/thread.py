"""
Module which contains the thread for poker players.
"""
from threading import Thread


class PokerPlayer(Thread):
    """
    Class which handles the poker player.
    """

    def __init__(self, name, cards):
        """"
        Constructor of the PokerPlayer class.
        """

        Thread.__init__(self)
        self.name = name
        self.cards = cards

    def run(self):
        """
        Method which prints the name of the player and what cards they have.
        """

        print("\n{} had ".format(self.name))

        for card in self.cards:
            print(" {}".format(card))
