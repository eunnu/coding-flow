from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split(" "))

ls = dict()
for _ in range(N):
    start, end = map(int, stdin.readline().split(" "))
    ls[start] = end

for _ in range(M):
    start, end = map(int, stdin.readline().split(" "))
    ls[start] = end

queue = deque()
queue.append((1, 0))
visit = set()
res = 100

while queue:
    location, cnt = queue.popleft()

    if location == 100:
        res = min(res, cnt)

    elif location > 100:
        break

    for i in range(1, 7):
        nl = location + i
        if nl in visit:
            continue
        if nl in ls:
            queue.append((ls[nl], cnt+1))
        elif nl not in ls:
            queue.append((nl, cnt+1))
        visit.add(nl)
        if nl > 100:
            break
print(res)