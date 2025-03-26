def action_1(l, a, b):
    for i in l:
        if a in i:
            l[b-1].append(a)
            i.remove(a)
            break
    return l

def action_2(l, a, b):
    tmp = l[a-1]
    l[a-1] = l[b-1]
    l[b-1] = tmp
    return l

def action_3(l, a):
    for idx, item in enumerate(l):
        if a in item:
            print(idx+1)
            break
    return None

n, actions = input().split()
n = int(n)
l = [[i+1] for i in range(n)]
for i in range(int(actions)):
    action_list = input().split()
    if len(action_list) == 3:
        action_type, a, b = action_list
        a = int(a)
        b = int(b)
    if len(action_list) == 2:
        action_type, a = action_list
        a = int(a)
    if action_type=='1':
        l = action_1(l, a, b)
    if action_type=='2':
        l = action_2(l, a, b)
    if action_type=='3':
        action_3(l, a)
