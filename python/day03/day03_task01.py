s1, s2, ans = input(), input(), 0
for i in range(1, len(s1) + 1):
    if ans == 0 and s2 == "".join(s1[j::i] for j in range(i)):
        ans = i
print(ans or "No")
