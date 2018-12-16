"""
Main module.
"""
from problem1 import thread
import IO

if __name__ == "__main__":

    queue = IO.get_queue(IO.get_number())

    sort_thread = thread.ThreadOverlord(queue)
    sort_thread.start()
