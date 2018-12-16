"""Module which contains the Anagram class."""
from itertools import permutations


class Anagram:
    """Class which handles anagrams creation."""

    def __init__(self, word):
        """Initialises the word for anagrams."""

        self.word = word
        self.counter = 0
        self.anagrams = []

        self.create_anagrams()

    def create_anagrams(self):
        """Creates anagrams for the word given at input."""

        self.anagrams = [''.join(perm) for perm in permutations(self.word)]

    def compare_anagrams(self, file):
        """Method which compares each anagram with each word from the dictionary.txt file."""

        with open(file, "r") as file:
            for line in file:
                if line[:-1] in self.anagrams:
                    print(line[:-1])
                    self.counter += 1

    def get_anagrams(self):
        """Returns the anagram list."""

        return self.anagrams

    def get_counter(self):
        """Returns the number of anagrams found in the dictionary."""

        return self.counter
