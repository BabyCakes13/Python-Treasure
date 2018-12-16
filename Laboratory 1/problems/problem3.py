def to_fahrenheit():
    """Gets the celsius degrees from the command line, transforms it into fahrenheit and prints."""

    celsius = int(input("give the temperature..."))

    fahrenheit = (9/5) * celsius + 32

    print(fahrenheit)


to_fahrenheit()
