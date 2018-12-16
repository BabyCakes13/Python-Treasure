"""Module which contains the shape classes."""
import math


class Shape:
    """Base class for the shapes."""

    def __init__(self):
        """Initialises the name and area."""
        self.name = ""
        self.area = 0

    def display(self):
        """Returns the name of the shape."""
        pass

    def getarea(self):
        """Returns the area of the shape."""
        pass


class Circle(Shape):
    """Class which contains the circle methods."""

    def __init__(self, radius):
        """Initialises the name and radius of the circle."""
        super(Circle, self).__init__()
        self.radius = radius
        self.name = "Circle"

    def getarea(self):
        """Returns the area of the circle."""
        self.area = math.pi * self.radius**2
        return self.area

    def display(self):
        """Returns the name of the circle."""
        return self.name


class Square(Shape):
    """Class which contains the square methods."""

    def __init__(self, side):
        """Initialises the name and side of the square."""
        super(Square, self).__init__()
        self.side = side
        self.name = "Square"

    def getarea(self):
        """Returns the area of the square."""
        self.area = self.side**2
        return self.area

    def display(self):
        "Returns the name of the square."
        return self.name


class Rectangle(Shape):
    """Class which contains the rectangle methods."""

    def __init__(self, length, width):
        """Initialises the sides and name of the rectangle."""
        super(Rectangle, self).__init__()
        self.length = length
        self.width = width
        self.name = "Rectangle"

    def getarea(self):
        """Returns the area of the rectangle"""
        self.area = self.length * self.width
        return self.area

    def display(self):
        """Returns the name of the rectangle."""
        return self.name


class Triangle(Shape):
    """Class which contains the triangle methods."""

    def __init__(self, a, b, c):
        """Initialises the name and sides of the triangle."""

        super(Triangle, self).__init__()
        self.a = a
        self.b = b
        self.c = c
        self.name = "Triangle"

    def getarea(self):
        """Returns the area of the triangle if it's a valid triangle."""

        if is_triangle([self.a, self.b, self.c]):
            semi = (self.a + self.b + self.c) / 2
            self.area = (semi * (semi - self.a) * (semi - self.b) * (semi - self.c))
            return self.area
        else:
            print("The triangle is not valid.")
            exit(-1)

    def display(self):
        """Returns the name of the shape."""
        return self.name


def is_triangle(sides):
    """Checks whether the triangle is a valid one."""

    smallest, medium, biggest = sorted(sides)

    return smallest + medium > biggest and all(s > 0 for s in sides)
