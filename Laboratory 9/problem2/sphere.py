"""
Module for cone thingy.
"""
from math import pi


class Sphere:
    """
    Class which handles cone thingy.
    """

    def __init__(self, radius):
        """
        Constructor of the Sphere class.
        :param radius: Radius of the sphere.
        """

        self.radius = radius

    def get_volume(self):
        """
        Method which returns the volume of the cone.
        :return: Volume of the cone.
        """

        return (4 / 3) * pi * (self.radius ** 3)
