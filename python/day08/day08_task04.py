class Smile:
    def __init__(self, size) -> None:
        self.size = size

    def __abs__(self):
        return abs(self.size)

    def __neg__(self):
        return Smile(-self.size)

    def __add__(self, other):
        return Smile(self.size + other.size)

    def __sub__(self, other):
        return Smile(self.size - other.size)

    def __mul__(self, num):
        return Smile(self.size * num)

    def __str__(self) -> str:
        size = abs(self.size)
        if size == 0:
            return ''
        if size == 1:
            return '/1\\\n|"|\n\\-/'
        # границы
        ret = ['|' + ' ' * (2 * size - 1) + '|' for i in range(size + 2)]
        ret[0] = '/' + f'{size:-<{size*2-1}}' + '\\'
        ret[-1] = '\\' + '-' * (size*2-1) + '/'

        shift = size // 4
        ind = shift
        if self.size < 0:
            ind = size - shift - 1
        ret[ind + 1] = '|' + ' ' * shift + 'O' + \
                       ' ' * (2 * size - 3 - 2 * shift) + \
                       'O' + ' ' * shift + '|'
        ret[-ind - 2] = '|' + ' ' * (shift + 1) + \
                        '-' * (2 * size - 3 - 2 * shift) + \
                        ' ' * (shift + 1) + '|'
        return '\n'.join(ret)
