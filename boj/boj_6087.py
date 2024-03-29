# dfs 방향이 바뀔 때 마다 +1
from collections import deque


W, H = map(int, input().split())
road_map = [list(input()) for _ in range(H)]

queue = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = set()

flag = False
for i in range(H):
    for j in range(W):
        if road_map[i][j] == 'C':
            queue.append((i, j, 0, -1))
            road_map[i][j] = 'S'
            flag = True
            break
    if flag:
        break

answer = 987654321
while queue:
    y, x, cnt, d = queue.popleft()
    visited.add((y, x))

    if answer < cnt:
        break

    if road_map[y][x] == 'C':
        answer = cnt

    for direc in range(4):
        ny = y + dy[direc]
        nx = x + dx[direc]

        if 0 <= ny < H and 0 <= nx < W and road_map[ny][nx] != '*':
            if (ny, nx) not in visited and answer > cnt:
                if d > -1 and d != direc:
                    queue.append((ny, nx, cnt+1, direc))
                else:
                    queue.append((ny, nx, cnt, direc))

print(answer)