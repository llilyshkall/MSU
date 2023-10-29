import itertools as it


def checkcomm(fun, *args):
    etal = fun(*args)
    for param in it.permutations(args):
        if etal != fun(*param):
            return False
    return True
