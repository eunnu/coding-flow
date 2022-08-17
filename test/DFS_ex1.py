def DFS_adj(n):
    if n not in visited:
        visited.append(n)

    for destination in range(len(adj_list[n])):
        if adj_list[n][destination] not in visited:
            DFS_adj(adj_list[n][destination])

V, E = map(int, input().split())

adj_list = [[] for _ in range(V + 1)]
map_list = list(map(int,input().split()))
visited = []

for i in range(E):
    start, end = map_list[i*2], map_list[i*2+1]
    adj_list[start].append(end)
    adj_list[end].append(start)

DFS_adj(1)
print(*visited)