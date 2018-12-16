def is_leap_year():
    """Takes an year given from command line and checks whether it is leap or not."""

    year = int(input("give the year..."))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("true")
    else:
        print("false")


is_leap_year()
