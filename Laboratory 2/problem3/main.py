def is_palindrome():
    """Checks whether a string is a palindrome."""

    string = input("give the string...")

    if string == string[::-1]:
        print("yes")
    else:
        print("no")


is_palindrome()