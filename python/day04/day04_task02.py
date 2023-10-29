def per(A=[-1, -1, -1, -1, -1], k=0):
    ret = []
    if k == 4:
        inv = 0
        for i in range(4):
            for j in range(i):
                if A[i] < A[j]:
                    inv += 1
        A[4] = inv
        ret = ret + A,
        A[4] = -1
        return ret
    for item in (0, 1, 2, 3):
        if item not in A:
            A[k] = item
            ret += per(A, k + 1)
            A[k] = -1
    return ret


def det4(r1, r2, r3, r4):
    P = per()
    A = (r1, r2, r3, r4)
    ret = 0
    for i in range(len(P)):
        mul = 1
        if P[i][4] % 2 == 1:
            mul = -1
        for j in range(len(P[i]) - 1):
            mul *= A[j][P[i][j]]
        ret += mul
    return ret
