from sys import stdin
from collections import deque


def solution():
    global n_tomato

    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    dh = [-1, 1]
    res = 0

    while queue:
        y, x, z, cnt = queue.popleft()
        res = max(res, cnt)

        for d in dh:
            if 0 <= d + z < H and not tomato[z+d][y][x] and (y, x, d + z) not in visit:
                queue.append((y, x, z+d, cnt+1))
                visit.add((y, x, z+d))
                tomato[z+d][y][x] = cnt
                n_tomato -= 1

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < N and 0 <= nx < M and not tomato[z][ny][nx] and (ny, nx, z) not in visit:
                queue.append((ny, nx, z, cnt + 1))
                visit.add((ny, nx, z))
                tomato[z][ny][nx] = cnt
                n_tomato -= 1

    if n_tomato:
        return -1
    else:
        return res


M, N, H = map(int, stdin.readline().split(" "))
tomato = []
queue = deque()
visit = set()
n_tomato = 0
for k in range(H):
    temp = [list(map(int, stdin.readline().split(" "))) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 1:
                queue.append((i, j, k, 0))
                visit.add((i, j, k))
            elif temp[i][j] == 0:
                n_tomato += 1
    tomato.append(temp)
print(solution())
