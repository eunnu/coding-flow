from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split(" "))
q = deque()
q.append((N, 1))
visit = set()
res = -1

while q:
    num, cnt = q.popleft()
    if num == M:
        res = cnt
        break

    if 2*num <= M and 2*num not in visit:
        q.append((num*2, cnt+1))

    if (num*10 + 1) <= M and (num*10 + 1) not in visit:
        q.append(((num*10 + 1), cnt+1))

print(res)