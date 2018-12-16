"""
Module which holds the sorting thread. It's a really cool thread.
"""
from threading import Thread, Lock


class ThreadOverlord(Thread):
    """
    Class which holds the sorting thread
    """

    def __init__(self, queue):
        """
        Constructor of the ThreadOverlord class.
        :param queue: The queue which contains the lists to be sorted.
        """

        Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        Method which sorts the lists in the queue.
        """

        lock = Lock()

        while not self.queue.empty():
            with lock:
                sorted_list = self.queue.get()
                sorted_list.sort()
                print(sorted_list)
