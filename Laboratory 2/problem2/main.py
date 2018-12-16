def revert_list():
    """Reverts a list given from command line."""

    text = input("give the list objects separated by space...\n").split(' ')[::-1]

    print(text)


revert_list()
