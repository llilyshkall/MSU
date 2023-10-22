N, M = map(int, input().split(','))

widthN = len(f'{N}')
widthNN = len(f'{N*N}')
widthCol = 2 * widthN + widthNN + 9

countCols = (M + 3) // widthCol
countRows = N // countCols
if N % countCols != 0:
  countRows += 1

line = "{:=^{width}}".format("", width=M)
print(line)
for row in range(countRows):
  for second in range(1, N + 1):
    print(*['{:.>{widthN}}.*.{:.<{widthN}}.=.{:.<{widthNN}}'.format(
          f'{first}', f'{second}', f'{first*second}', widthN=widthN, widthNN=widthNN) 
          for first in range(row * countCols + 1, min((row + 1) * countCols, N) + 1)],
          sep='.|.')
  print(line)
