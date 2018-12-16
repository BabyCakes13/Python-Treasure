class Converter:
    """Class which converts input from command line to morse code."""
    
    def __init__(self):
        """The code is converted from the morse.txt file.
        The text is given at command line."""
        
        self.code = get_code("morse.txt")
        self.text = input("give the text...\n").upper()

    def convert(self):
        """Method which converts the latin text to morse."""

        morse = ""

        for character in self.text:
            if character in self.code.keys():
                morse += self.code.get(character, ' ') + "  "
            elif character == " ":
                morse += "  "
            else:
                morse += character

        return morse


def get_code(file):
    """Method which returns the dictionary from the file."""

    text = []
    with open(file, "r") as file:
        for line in file:
            text = text.append(line)

    code = {}
    for i in range(len(text)):
        text[i] = text[i][:-1].split(':')
        code[text[i][0]] = text[i][1][1:]

    return code
