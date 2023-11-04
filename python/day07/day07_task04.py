import decimal
import random

data = {}


def split_bin(a, b):
    global data
    if b != a + 1:
        med = (a + b) // 2
        if data.get((a, med)) is None:
            data[(a, med)] = split_bin(a, med)
        p_left, q_left, r_left = data[(a, med)]

        if data.get((med, b)) is None:
            data[(med, b)] = split_bin(med, b)
        p_right, q_right, r_right = data[(med, b)]

        p = p_left * p_right
        q = q_left * q_right
        r = q_right * r_left + p_left * r_right
    else:
        p = -(6*a - 5)*(2*a - 1)*(6*a - 1)
        q = 10939058860032000 * a**3
        r = p * (545140134*a + 13591409)
    data[(a, b)] = p, q, r
    return p, q, r


def chudnovsky(n):
    p, q, r = split_bin(1, n)
    return (426880 * decimal.Decimal(10005).sqrt() * q) / (13591409*q + r)


def PiGen():
    decimal.getcontext().prec = 1500
    old_pi = chudnovsky(2) % 1 * 10
    new_pi = chudnovsky(3) % 1 * 10
    ch = 4
    yield '3'
    yield '.'
    for i in range(1, 10000):
        c1, c2 = old_pi // 1, new_pi // 1
        # print(c1, old_pi)
        # print(c2, new_pi)
        # print()
        if c1 != c2:
            old_pi = new_pi

            new_pi = chudnovsky(ch) * (decimal.Decimal(10) ** i) % 10
            # print(new_pi)
            ch += 1
            # break
        yield str(c2)
        old_pi = old_pi % 1 * 10
        new_pi = new_pi % 1 * 10

    while True:
        yield str(random.randint(0, 9))
