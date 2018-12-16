"""
Module for cone thingy.
"""
from math import pi


class Cone:
    """
    Class which handles cone thingy.
    """

    def __init__(self, radius, height):
        """
        Constructor of the Cylinder class.
        :param radius: Radius of the cone.
        :param height: Height of the cone.
        """

        self.radius = radius
        self.height = height

    def get_volume(self):
        """
        Method which returns the volume of the cone.
        :return: Volume of the cone.
        """

        return (1 / 3) * pi * (self.radius ** 2) * self.height
