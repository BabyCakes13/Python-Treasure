from problem1 import thread
from threading import Event
import time
import IO


def wait_semaphore(event):
    """
    Method which waits for the semaphore to be set.
    :param event: Even for waiting.
    """
    event.wait()


if __name__ == "__main__":

    number = IO.get_number()
    semaphore = Event()

    for i in range(number):
        t = thread.CarThread(name="Car " + str(i), target=wait_semaphore, args=(semaphore,))
        t.start()

    colors = ['RED', 'YELLOW', 'GREEN']

    for color in colors:
        print(color)
        time.sleep(1)

    semaphore.set()
