def format_phone():
    """Takes a phone number from the command line and """

    number = input("give the telephone number...\n")

    format1 = "({}){}".format(number[:4], number[4:])
    format2 = "{}-{}".format(number[:4], number[4:])
    format3 = "{}-{}-{}".format(number[:3], number[3:6], number[6:])

    print("{}\n{}\n{}\n".format(format1, format2, format3))


format_phone()
