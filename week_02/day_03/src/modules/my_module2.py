myVar = 10


def myFunction(p1, p2):
    """
    Docstring for myFunction

    :param p1: Description
    :param p2: Description
    """
    print("myFunction() was entered")
    return p1, p2


if (
    __name__ == "__main__"
):  # Checks if this script is run directly. If it is run as a module in another script, the name is not "__main__".
    print(myFunction(1, 2))
