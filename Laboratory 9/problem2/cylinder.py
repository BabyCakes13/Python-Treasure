"""
Module for cylinder thingy.
"""
from math import pi


class Cylinder:
    """
    Class which handles cylinder thingy.
    """

    def __init__(self, radius, height):
        """
        Constructor of the Cylinder class.
        :param radius: Radius of the cylinder.
        :param height: Height of the cylinder.
        """

        self.radius = radius
        self.height = height

    def get_volume(self):
        """
        Method which returns the volume of the cylinder.
        :return: Volume of the cylinder.
        """

        return pi * (self.radius ** 2) * self.height
