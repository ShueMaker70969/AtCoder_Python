import collections
l = input().split()
c = collections.Counter(l)
v = list(c.values())
has_three = False
has_two = False
for i in v:
    if i>=3 and has_three==False:
        has_three = True
    elif i>=2:
        has_two = True
if has_three and has_two:
    print('Yes')
else:
    print('No')