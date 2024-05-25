# 백준 쉬운 최단 거리 - 실버 1
# 그래프 이론, 그래프 탐색, bfs
# 목표 지점부터 탐색 후에 해당 좌표에서부터 거리를 탐색해야 할 듯.
# 0으로 막혀있는 부분들은 옆에 숫자보다 +1 해주면 될 것 같음.


import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split(" "))
ground = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]
deq = deque()
visit_ground = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if ground[i][j] == 2:
            deq.append((i, j, 0))
        elif ground[i][j] == 0:
            visit_ground[i][j] = 0

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
while deq:
    y, x, cnt = deq.popleft()
    if 1 > visit_ground[y][x] or visit_ground[y][x] > cnt:
        visit_ground[y][x] = cnt

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or ny >= n or nx >= m or ground[ny][nx] != 1:
            continue
        else:
            if 0 < visit_ground[ny][nx] <= cnt + 1:
                continue
            else:
                visit_ground[ny][nx] = cnt + 1
                deq.append((ny, nx, cnt + 1))


for i in range(n):
    for j in range(m - 1):
        print(visit_ground[i][j], end=" ")
    print(visit_ground[i][m-1])