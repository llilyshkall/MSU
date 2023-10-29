def joinseq(*args):
    iters = [iter(item) for item in args]
    data = [next(it) for it in iters]
    while data:
        m = 0
        for i in range(len(data)):
            if data[i] < data[m]:
                m = i

        yield data[m]
        data[m] = next(iters[m], None)
        if data[m] is None:
            del data[m]
            del iters[m]
