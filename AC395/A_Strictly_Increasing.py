def is_increasing(n, l):
    for i in range(n-1):
        if int(l[i])<int(l[i+1]):
            pass
        else:
            return 'No'
    return 'Yes'

n = int(input())
str = input()
l = str.split()
print(is_increasing(n, l))