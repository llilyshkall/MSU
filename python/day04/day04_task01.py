def sheff(A, B):
    ret = 0
    a, b = bool(A), bool(B)
    if a == b:
        ret = not a
    else:
        ret = A or B
    return ret
