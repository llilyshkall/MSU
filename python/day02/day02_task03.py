N = 1
name = eval(input())
while a := input():
  if eval(a) != name:
    N -= 1
    if N == 0:
      name = eval(a)
      N = 1
  else:
    N += 1

print(name)