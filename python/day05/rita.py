N, M = eval(input())
print('='*M)
a = int(len(str(N)))
b = int(len(str(N**2)))
max = (M+3)//(9+2*a+b)
A = N//max
if N%max>0:
    A += 1
for i in range(A):
    s = ''
    for k in range(1, N+1):
        B = (i+1)*max+1
        if B>=N:
            B = N+1
        print(*['{:.>{a}}.*.{:.<{a}}.=.{:.<{b}}'.format(str(j),str(k),str(j*k),a=a, b=b)
                for j in range(i*max+1,B)], sep='.|.')
    print('='*M)