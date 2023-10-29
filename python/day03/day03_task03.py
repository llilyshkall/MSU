s1 = input()
ans = 0
if (s1):
    n = len(s1)
    while s2 := input():
        for i in range(n - 1):
            if s1[i] == '#' and s1[i + 1] == '.' and s2[i] == '.':
                ans += 1
        if s1[n - 1] == '#' and s2[n - 1] == '.':
            ans += 1
        s1 = s2
    for i in range(n - 1):
        if s1[i] == '#' and s1[i + 1] == '.':
            ans += 1
    if s1[n - 1] == '#':
        ans += 1

print(ans)
