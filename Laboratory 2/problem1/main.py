import re


def count_words():
    """Counts the words from a text."""

    text = get_file().replace('\n', ' ').split(' ')

    print("Number of words: {}".format(len(text)))


def count_vowels():
    """Counts the number of vowels from a text."""

    vowels = len(re.findall('[aeiou]', get_file()))

    print("Number of vowels: {}".format(vowels))


def get_file():
    """Opens the text file and stores it in a variable."""

    file = open("text", "r", encoding="utf-8")

    text = file.read()

    file.close()

    return text


count_words()
count_vowels()
