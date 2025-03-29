n = input()
l1 = list(input())
l2 = list(input())
cnt = 0
for i in range(len(l1)):
    if l1[i] != l2[i]:
        cnt += 1
print(cnt)