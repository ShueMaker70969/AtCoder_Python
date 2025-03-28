s = input()
l = list(s)
i = 0
while i < len(l):
    if len(l) < 2:
        break
    if l[i]=='(' and l[i+1]==')':
        l.pop(i)
        l.pop(i)
        if i > 0:
            i -= 2
        else:
            i -= 1
    elif l[i]=='[' and l[i+1]==']':
        l.pop(i)
        l.pop(i)
        if i > 0:
            i -= 2
        else:
            i -= 1
    elif l[i]=='<' and l[i+1]=='>':
        l.pop(i)
        l.pop(i)
        if i>0:
            i -= 2
        else:
            i -= 1
    i += 1
if l:
    print('No')
else:
    print('Yes')
