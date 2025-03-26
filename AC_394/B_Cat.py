n = int(input())
l = []
for i in range(n):
    l.append(input())
l = sorted(l, key=len)
for i in l:
    print(i, end='')
