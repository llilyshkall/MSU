N = int(input())
A = 1
B = int(N ** (1 / 3))
ans = 0

while A <= B:
    sum = (A ** 3) + (B ** 3)
    if sum > N:
        B -= 1
    else:
        A += 1
        if sum == N:
            ans += 1

print(ans)
