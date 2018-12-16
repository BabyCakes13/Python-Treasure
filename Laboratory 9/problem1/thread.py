"""
Module which contains the Car thread.
"""
from threading import Thread
import random


class CarThread(Thread):
    """
    Class which handles the baby car race.
    """

    def __init__(self, name, target, args):
        """
        Constructor of the CarThread class.
        :param name: Name of the car
        :param target: Method for the thread.
        :param args: Arguments of the method.
        """

        Thread.__init__(self, target=target, args=args)
        self.name = name
        self.delay = 0

    def run(self):
        """
        Method which sets the delay time and starts start_car.
        """

        super(CarThread, self).run()
        self.delay = random.randint(1, 5)
        self.start_car()

    def start_car(self):
        """
        Just a tiny method to print the car status.
        """

        print("{} started after {} seconds".format(self.name, self.delay))
