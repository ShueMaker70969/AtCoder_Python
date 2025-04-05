n, m = input().split()
sum = 0
for i in range(int(m)+1):
   sum += pow(int(n), i)
if sum <= pow(10, 9):
    print(sum)
else:
    print('inf')