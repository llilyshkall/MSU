

class Geom:
    def __init__(self, base, deno, start = 0, end = None) -> None:
        self.base = base
        self.deno = deno
        self.start = start
        self.end = end
    
    def __getitem__(self, index):
        if index == ... or type(index) == tuple:
            start = 0
            end = None
            if index != ...:
                if len(index) == 3:
                    start = index[0]
                    end = index[2]
                if len(index) == 2:
                    start = index[0] if index[1] == ... else 0
                    end = index[1] if index[0] == ... else None
            return Geom(self.base, self.deno, start, end)
        elif type(index) is slice:
            if index.start is None and index.stop is None and index.step is None:
                return Geom(self.base, self.deno)
            ret = [self[i] for i in range(index.start or 0, index.stop or -1, index.step or 1)]
            return ret
        else:
            return self.base * (self.deno ** index)
    
    def __iter__(self):
        self.n = self.start
        return self
    
    def __next__(self):
        if self.n >= 0 and (self.end is None or self.n < self.end):
            ret = self.base * (self.deno ** self.n)
            self.n = self.n + 1
            return ret
        else:
            raise StopIteration


# g = Geom(3, 2)
# print(*zip("012345", g[::]))
# print(*zip("012345", g[:]))
# print(*g[..., 11])
# print(*zip(g[20, ...], "0123"))