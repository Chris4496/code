import shelve


def isbettable(i, name):
    file = shelve.open(name)
    if i == "":
        return False
    try:
        i = int(i)
    except ValueError:
        return False
    if i > file['value2']:
        return False
    return True
