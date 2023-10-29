s = eval(input())
n = len(s)

coord = [(s[i][0], False) for i in range(n)] + [(s[i][1], True) for i in range(n)]
coord.sort()

ans = 0
c = 0
for i in range(n*2):
    if c != 0 and i > 0:
        ans += coord[i][0] - coord[i-1][0]
    if coord[i][1]:
        c += 1
    else:
        c -= 1

print(ans)
