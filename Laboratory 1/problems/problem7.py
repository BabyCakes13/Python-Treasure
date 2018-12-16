def check_number():
    """Takes a number form the command line and checks whether is is positive, negative or zero."""

    number = int(input("give the number...\n"))

    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")


check_number()
