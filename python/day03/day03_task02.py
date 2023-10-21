m, n = input().split(',')
n = int(n)
m = int(m)
num = 0

A = [[0] * m for i in range(n)]

for s in range(n + m - 1):
  i = 0
  j = 0
  step_i = 0
  step_j = 0
  if s % 2 == 1:
    i = min(s, n - 1)
    j = s - i
    step_i = -1
    step_j = 1
  else:
    j = min(s, m - 1)
    i = s - j
    step_i = 1
    step_j = -1
  
  A[i][j] = 9

  while -1 < i and i < n and -1 < j and j < m:
    A[i][j] = num
    num += 1
    if num > 9:
      num = 0
    (i, j) = (i + step_i, j + step_j)

for i in range(n):
  print(*A[i])
