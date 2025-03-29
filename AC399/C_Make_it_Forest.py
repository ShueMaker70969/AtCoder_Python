def dfs(node):
    visited[node] = True
    for next_node in e[node]:
        if not visited[next_node]:
            dfs(next_node)


n, m = map(int, input().split())
e = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

groups = 0
for i in range(1, n + 1):
    if not visited[i]:
        groups += 1
        dfs(i)

print(m - (n - groups))