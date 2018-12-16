def check_divisible():
    """Stores in a list the elements from 1000 to 2000 which are divisible by 7 but not by 5."""

    result = []
    for i in range(1000, 2000):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)

    print("result: {}".format(result))


check_divisible()

