def swap():
    """Takes two numbers from the command line and swaps their value."""

    a = int(input("give the first number...\n"))
    b = int(input("give the second number...\n"))

    a, b = b, a

    print("a = {} \nb = {}".format(a, b))


swap()
