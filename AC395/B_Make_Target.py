n = int(input())
l = [['#' for i in range(n)]for i in range(n)]
for i in range(1, n):
    j = n + 1 - i
    if i <= j:
        if i%2 == 0:
            for x in range(i-1, j):
                for y in range(i-1, j):
                    l[x][y] = '.'
        elif i%2 == 1:
            for x in range(i-1, j):
                for y in range(i-1, j):
                    l[x][y] = '#'
for i in range(n):
    for j in range(n):
        print(l[i][j], end="")
    print('')
