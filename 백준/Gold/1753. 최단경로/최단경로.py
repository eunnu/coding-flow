import heapq
from sys import stdin

N, M = map(int, stdin.readline().split(" "))
start_node = int(stdin.readline())
graph = [list() for _ in range(N+1)]

for i in range(M):
    node, end, cost = map(int, stdin.readline().split(" "))
    graph[node].append([end, cost])

queue = []
heapq.heappush(queue, (0, start_node))
res = [float('inf')]*(N+1)
res[start_node] = 0

while queue:
    cost, node = heapq.heappop(queue)
    if cost > res[node]:
        continue

    for i in graph[node]:
        if res[i[0]] > cost + i[1]:
            res[i[0]] = cost + i[1]
            heapq.heappush(queue, (cost+i[1], i[0]))

for i in range(1, N+1):
    if res[i] == float("inf"):
        print("INF")
    else:
        print(res[i])