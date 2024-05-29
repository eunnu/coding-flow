import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
res = 0
queue = deque()
campus = []
for i in range(N):
    temp = []
    a = sys.stdin.readline()
    for j in range(M):
        if a[j] == "I":
            queue.append((i, j))
            temp.append(2)
        elif a[j] == "O":
            temp.append(1)
        elif a[j] == "X":
            temp.append(0)
        elif a[j] == "P":
            temp.append(3)
    campus.append(temp)
visit = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    y, x = queue.popleft()

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or ny >= N or nx < 0 or nx >= M or (ny, nx) in visit or campus[ny][nx] == 0:
            continue
        elif campus[ny][nx] == 3:
            res += 1
        queue.append([ny, nx])
        visit.add((ny, nx))

if res:
    print(res)
else:
    print("TT")