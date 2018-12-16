class Class:
    """Class which contains the transform methods."""

    def __init__(self):
        """Initialises the string."""

        self.string = ""

    def ask_str(self):
        """Gets the string from the user."""

        self.string = input("give the string...")

    def transform_str(self):
        """Prints the transformed string."""

        print(self.string.upper())


def class_test():
    """Tests the class."""

    test = Class()
    test.ask_str()
    test.transform_str()


if __name__ == "__main__":
    class_test()
