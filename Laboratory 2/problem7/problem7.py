def operate_array():
    """Given an array, it removes the duplicates, min, max and computes the average."""

    array = list(map(int, input("give the array...\n").split(' ')))

    array = set(array)

    array.remove(min(array))
    array.remove(max(array))

    print("array: {}".format(array))
    print("average: {}".format(int(sum(array)) // max(len(array), 1)))


operate_array()
