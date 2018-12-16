from problem1 import converter


def init():
    """Calls the converter to convert the input."""

    convert = converter.Converter()
    print(convert.convert())


init()
