"""
Module which contains filter examples.
"""
import util


def text():
    """
    Method which contains the text.
    :return: A string representing the future list of words.
    """
    return "Now is the winter of our discontent" \
           " Made glorious summer by this sun of York;" \
           " And all the clouds that lour'd upon our house " \
           "In the deep bosom of the ocean buried. "


def filter_text(string):
    """
    Method which splits the given string into words.
    Checks which elements have length greater than 4 and creates a list with those.
    :param string: A string formed of words.
    :return: A list formed of words from that string with length greater or equal than 4.
    """

    words = string.split(' ')

    filtered = filter(lambda x: len(x) >= 4, words)

    return filtered


if __name__ == "__main__":

    print("WORDS WITH LENGTH >= 4: \n")

    util.pretty_print(filter_text(text()))
