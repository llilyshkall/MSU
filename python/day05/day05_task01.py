s = input()
pattern = input()
ans = -1
for i in range(len(s) - len(pattern) + 1):
    check = True
    for j in range(len(pattern)):
        if pattern[j] != '@':
            if s[i + j] != pattern[j]:
                check = False
                break
    if check:
        ans = i
        break
print(ans)
