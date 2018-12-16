"""
Module which contains the facade for pretty computing the volume of the weird shape.
"""
from problem2.cone import Cone
from problem2.cube import Cube
from problem2.cylinder import Cylinder
from problem2.sphere import Sphere


class Facade:
    """
    Class which generates a facade for computing the weirdly shaped object.
    """

    def __init__(self):
        """
        Constructor of the Facade class.
        """

        self.cone = Cone(3, 5)
        self.cube = Cube(3)
        self.cylinder = Cylinder(3, 7)
        self.sphere = Sphere(3)

    def get_volume(self):
        """
        Method which computes the volume of the weird shape.
        :return: The volume of the shape.
        """

        attributes = [self.cone, self.cube, self.cylinder, self.sphere]
        volume = 0

        for a in attributes:
            volume += a.get_volume()

        return round(volume, 2)
