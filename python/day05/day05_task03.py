import random


def divrandom(a, b, s, p):
    m, M = min(a, b), max(a, b)
    i = m
    while i % p == 0 and i <= M:
        i += s
    if i % p == 0:
        return 0
    i = 0
    while i % p == 0:
        i = random.randrange(m, M + 1, s)
    return i
