"""
Module which holds the cube thingy.
"""


class Cube:
    """
    Class which handles the cube thingy.
    """

    def __init__(self, side):
        """
        Constructor for the Cube class.
        :param side:
        """

        self.side = side

    def get_volume(self):
        """
        Method which computes the volume of the cube.
        :return: Volume of the cube.
        """

        return self.side ** 3
