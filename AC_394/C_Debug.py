s = input()
l = list(s)
i = 0
while i < len(l)-1:
    if l[i]=='W' and l[i+1] == 'A':
        l[i] = 'A'
        l[i+1] = 'C'
        if i>0:
            i -= 1
    else:
        i += 1
for i in l:
    print(i, end='')