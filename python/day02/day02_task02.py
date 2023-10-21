max = int(input())
sec = 0

while (item := int(input())) != 0:
  if item > max:
    sec = max
    max = item
  elif item != max:
    if sec < item or sec == 0:
      sec = item

if sec:
  print(sec)
else:
  print("NO")
