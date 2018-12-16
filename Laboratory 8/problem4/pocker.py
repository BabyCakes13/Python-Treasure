"""
Module which holds the Card Package class.
"""


class CardPackage:
    """
    Class which handles card package.
    """

    def __init__(self):
        """
        Constructor for the CardPackage class.
        """

        self.card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
        self.colors = ["heart", "diamond", "spade", "club"]

    def create_package(self):
        """
        Method which creates the card package.
        :return: The card package.
        """

        card_package = []

        for number in self.card_values:
            for color in self.colors:
                card_package.append("{} of {}".format(number, color))

        return card_package
