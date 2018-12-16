"""
Module which forced players to play poker as the overlord wants to.
"""
from problem4.pocker import CardPackage
from problem4.thread import PokerPlayer
from queue import Queue
import IO
import random

if __name__ == "__main__":

    card_package = CardPackage().create_package()
    random.shuffle(card_package)

    card_queue = Queue()

    number = IO.get_number()

    for i in range(number):
        random_number = random.randint(0, len(card_package) - 6)
        card_queue.put(card_package[random_number:random_number + 5])

    for i in range(number):
        t = PokerPlayer(name="Player-" + str(i), cards=card_queue.get())
        t.start()
