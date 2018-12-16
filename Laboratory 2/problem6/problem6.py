def get_factorial():
    """Given a number from command line, computes the factorial and displays it."""

    number = int(input("give the number..."))

    for i in range(1, number):
        number *= i

    print("factorial: {}".format(number))


get_factorial()
