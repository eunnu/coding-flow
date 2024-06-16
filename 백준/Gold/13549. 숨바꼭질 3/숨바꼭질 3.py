from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split(" "))
queue = deque()
queue.append(N)
visit = [-1]*200010
visit[N] = 0
res = 100001

while queue:
    d = queue.popleft()
    s = visit[d]
    if d == M:
        res = min(res, s)

    if d + 1 <= M + 3 and (visit[d+1] < 0 or visit[d+1] > s+1):
        queue.append(d+1)
        visit[d+1] = s+1
    if d - 1 >= 0 and (visit[d-1] < 0 or visit[d-1] > s+1):
        queue.append(d-1)
        visit[d-1] = s+1
    if M*2 > 2*d > 0 and (visit[d*2] < 0 or visit[d*2] > s):
        queue.append(d*2)
        visit[2*d] = s

print(res)