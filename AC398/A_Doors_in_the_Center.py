import math
n = int(input())
for i in range(int(math.ceil(n/2)-1)):
    print('-', end='')
if n%2 == 0: print('==', end='')
elif n%2 != 0: print('=', end='')
for i in range(int(math.ceil(n/2)-1)):
    print('-',end='')