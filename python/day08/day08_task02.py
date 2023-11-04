from math import isclose


class Triangle:
    exist = True

    def __init__(self, a, b, c) -> None:
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.exist = a + b > c and a + c > b and b + c > a \
            and a > 0 and b > 0 and c > 0

    def __str__(self) -> str:
        return f'{self.a}:{self.b}:{self.c}'

    def __abs__(self) -> float:
        ret = 0
        if self.exist:
            p = sum([self.a, self.b, self.c]) / 2
            ret = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return ret

    def __bool__(self) -> bool:
        return self.exist

    def __eq__(self, __value: object) -> bool:
        ret = True
        length1 = sorted([self.a, self.b, self.c])
        length2 = sorted([__value.a, __value.b, __value.c])
        for l1, l2 in zip(length1, length2):
            ret = ret and isclose(l1, l2)
        return ret

    def __ne__(self, __value: object) -> bool:
        return not (self == __value)

    def __lt__(self, __value: object) -> bool:
        return abs(self) < abs(__value)

    def __le__(self, __value: object) -> bool:
        return abs(self) <= abs(__value)

    def __gt__(self, __value: object) -> bool:
        return abs(self) > abs(__value)

    def __ge__(self, __value: object) -> bool:
        return abs(self) >= abs(__value)
