from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split(" "))
relation = [[0] * (N + 1) for _ in range(N + 1)]
visit = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, stdin.readline().split(" "))
    relation[start][end], relation[end][start] = 1, 1
    visit[start][end], visit[end][start] = 1, 1

queue = deque()

for i in range(1, N + 1):
    queue.append((i, i, 0))

visited = set()
while queue:
    num, enum, cnt = queue.popleft()

    for i in range(1, N + 1):
        if i == num:
            continue
        if (num, i) in visited:
            continue
        if relation[enum][i]:
            visited.add((num, i))
            queue.append((num, i, cnt+1))
            if not visit[num][i]:
                visit[num][i] = cnt+1

res = []
for i in range(1, N + 1):
    res.append([sum(visit[i]), i])
res.sort()
print(res[0][1])
