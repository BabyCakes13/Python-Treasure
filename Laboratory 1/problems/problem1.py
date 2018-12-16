def get_maximum():
    """Gets three numbers from the command line and finds the maximum between them."""

    a = int(input("give the first number...\n"))
    b = int(input("give the second number...\n"))
    c = int(input("give the third number...\n"))

    print("maximum: ")
    if a > b and a > c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)


get_maximum()

