def change_occurrences():
    """Takes a string from the command line and replaces all the occurrences"""

    string = input("give the string...")
    string = string[0] + string[1:].replace(string[0], "$")

    print(string)


change_occurrences()
