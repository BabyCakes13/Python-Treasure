from problem3 import anagram

if __name__ == '__main__':

    word = input("give the word...")

    # contains the anagrams of the word
    anagrams = anagram.Anagram(word)

    print("ANAGRAMS: {}\n".format(anagrams.get_anagrams()))

    # compare the anagrams with the dictionary
    anagrams.compare_anagrams("files\dictionary.txt")

    print("\nFOUND: {} anagrams".format(anagrams.get_counter()))


