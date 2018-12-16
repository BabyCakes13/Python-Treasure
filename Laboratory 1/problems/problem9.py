def delete_strings():
    """Takes a string from command line and deletes all * and the neighbour letters from it."""

    string = input("give the string...")
    position = string.find("*")

    while position != -1:
        if position == 0:
            string = string[:position] + string[position+2:]
        if position == len(string):
            string = string[:position-1] + string[position+1:]
        else:
            string = string[:position-1] + string[position+2:]
        position = string.find("*")

    print(string)


delete_strings()
