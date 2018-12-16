def create_dict(a, b):
    """Creates a dictionary formed of keys from the interval [a, b]
    and values being the square of the keys."""

    keys = range(a, b)
    values = [i**2 for i in keys]

    return dict(zip(keys, values))


print(create_dict(1, 30))
