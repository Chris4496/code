import shelve


def isbettable(i, money):
    if i == "":
        return False
    try:
        i = int(i)
    except ValueError:
        return False
    if i > money:
        return False
    return True
