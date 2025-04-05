import math
def is_square(int):
    if int == 1:
        return True
    x = int // 2
    seen = set([x])
    while x * x != int:
        x = (x + (int // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

n = int(input())
cnt = 0
for i in range(2, n+1):
    x = i
    if i%2 == 0:
        while x > 0:
            if (is_square(x)):
                cnt += 1
                break
            else:
                if x%2 == 1:
                    break
                x = int(x / 2)
print(cnt)