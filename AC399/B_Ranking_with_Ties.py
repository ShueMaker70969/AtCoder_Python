import numpy as np

n = int(input())
l1 = input().split(' ')
for i in range(len(l1)):
    l1[i] = int(l1[i])
l2 = [0] * n

r = 1
while r < len(l1)+1:
    max_indices = []
    #obtain higest value
    max_val = np.max(l1)
    for i in range(len(l1)):
        if l1[i] == max_val:
            max_indices.append(i)
            l1[i] = -1
    for i in max_indices:
        l2[i] = r
    r += len(max_indices)
for i in l2:
    print(i)