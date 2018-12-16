def odd_even():
    """Gets a number form the command line and prints whether the number is odd or even."""

    number = int(input("give the number...\n"))

    if number%2 == 0:
        print("even")
    else:
        print("odd")


odd_even()
