def gen(num, beg=2,A=[]):
  if num == 1:
    if A:
      print(*A,sep='*')
  else:
    for i in range(beg, int(num ** 0.5 + 1)):
      if num % i == 0:
        gen(num // i, i, A + [i])
    else:
      gen(1, num, A + [num])

num = int(input())
gen(num)