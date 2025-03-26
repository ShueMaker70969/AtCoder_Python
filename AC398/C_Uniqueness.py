import collections
n = input()
l = input().split()
c = collections.Counter(l)
unique_items = []
for i in c.items():
    if i[1] == 1:
        unique_items.append(i)
if unique_items:
    max = 0
    for i in unique_items:
        if int(i[0]) > max:
            max = int(i[0])
    print(l.index(str(max))+1)
else:
    print('-1')