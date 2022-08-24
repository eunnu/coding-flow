N, E = map(int, input().split())
load = list(map(int, input().split()))

bfs_map = [[0]*(N+1) for i in range(N+1)]

for i in range(0, E):
    bfs_map[load[2*i]][load[2*i+1]] = 1

queue = [1]
visit = []

while queue:
    idx = queue.pop(0)

    if idx not in visit:
        visit.append(idx)

    for i in range(N+1):
        if bfs_map[idx][i] and i not in visit:
            queue.append(i)

print(*visit)