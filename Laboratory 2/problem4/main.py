def find_common_elements():
    """Creates and displays a list formed of the common elements of two lists"""

    list1 = set((input("give the first list separated by space...").split(' ')))
    list2 = set((input("give the first list separated by space...").split(' ')))

    result = list1.intersection(list2)

    print(result)


find_common_elements()
