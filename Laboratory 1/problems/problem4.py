def to_celsius():
    """Gets the fahrenheit degrees from the command line, transforms it into celsius and prints."""

    fahrenheit = int(input("give the temperature..."))

    celsius = (5/9) * (fahrenheit - 32)

    print(celsius)


to_celsius()
