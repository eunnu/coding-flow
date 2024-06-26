import heapq
import sys

inp = sys.stdin.readline
N = int(inp())
M = int(inp())
INF = 987654321
dist = [INF] * (N + 1)  # 시작노드에서부터 v로 가는 최소 비용
graph = [[] for _ in range(N + 1)]  # [v1에서][v2, v2로 가는 비용]

for _ in range(M):
    v1, v2, cost = map(int, inp().split(" "))
    graph[v1].append((v2, cost))

s_p, e_p = map(int, inp().split(" "))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, node = heapq.heappop(q)
        if distance > dist[node]:
            continue

        for n in graph[node]:
            new_cost = n[1] + distance  # v2로 가는 노드의 거리 + 내가 방금 빼낸 관심노드까지의 최단거리
            if new_cost < dist[n[0]]:  # v2까지의 거리보다 짧으면
                dist[n[0]] = new_cost
                heapq.heappush(q, (new_cost, n[0]))


dijkstra(s_p)
print(dist[e_p])