from sys import stdin

N = int(stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N - 1):
    start, end = map(int, stdin.readline().split(" "))
    graph[start].append(end)
    graph[end].append(start)

res = [0] * (N+1)
queue = [1]
visit = [0] * (N+1)

while queue:
    node = queue.pop()
    for i in graph[node]:
        if not visit[i]:
            res[i] = node
            visit[i] = 1
            queue.append(i)
for i in range(2, N + 1):
    print(res[i])