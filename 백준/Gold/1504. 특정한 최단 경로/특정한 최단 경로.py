from sys import stdin
import heapq

INF = 987654321
inp = stdin.readline
N, M = map(int, inp().split(" "))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, inp().split(" "))
    graph[a].append([b, c])
    graph[b].append([a, c])
n1, n2 = map(int, inp().split(" "))
res = []


def solution(start):
    q = []
    d = [[INF, i] for i in range(N + 1)]
    heapq.heappush(q, [0, start])
    d[start][0] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > d[now][0]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < d[i[0]][0]:
                d[i[0]][0] = cost
                d[i[0]][1] = i[0]

                heapq.heappush(q, [cost, i[0]])
    res.append(d)


solution(1)
solution(n1)
solution(n2)
res1 = res[0][n1][0] + res[1][n2][0] + res[2][N][0]
res2 = res[0][n2][0] + res[2][n1][0] + res[1][N][0]
print(min(res1, res2) if min(res1, res2) < INF else -1)