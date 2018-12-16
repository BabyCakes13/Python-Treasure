"""Module which holds the Player class."""


class Player:
    """Class which holds the Player methods."""

    def __init__(self, amount, army):
        """Initialises a player with an amount and army."""

        self.amount = amount
        self.army = army

    def get_amount(self):
        """Returns the amount of money the player currently has."""

        return self.amount

    def set_amount(self, amount):
        """Sets the amount of money the player has."""

        self.amount = amount
