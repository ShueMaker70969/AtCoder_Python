str = input()
l = list(str)
cnt = 0
for i in l:
    if i == '2':
        cnt += 1
print('2'*cnt)