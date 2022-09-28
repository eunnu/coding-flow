# 완전한 시뮬
# 1. 벽을 세개 세우고
# 2. 바이러스를 퍼뜨려서 안전한 곳을 센다.
# 매번 배열을 복사 할 수 없으므로 가상 좌표를 사용
from collections import deque


def bfs():
    global ans
    safe_zone = len(safe)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = set()

    flag = False
    for vi in v:
        queue.append(vi)

    while queue:
        (y, x) = queue.popleft()

        visited.add((y, x))

        if ans and safe_zone < ans:
            flag = True
            break

        for direc in range(4):
            ny = y + dy[direc]
            nx = x + dx[direc]

            if 0 <= ny < r and 0 <= nx < c:
                if (ny, nx) not in visited:
                    if (ny, nx) in safe:
                        queue.append((ny, nx))
                        safe_zone -= 1

    if not flag and ans < safe_zone:
        ans = safe_zone


def add_wall(cnt):
    if cnt == 3:
        bfs()
        return

    else:
        for idx in range(r):
            for jdx in range(c):
                if (idx, jdx) in safe:
                    safe.discard((idx, jdx))
                    wall.add((idx, jdx))
                    add_wall(cnt + 1)
                    wall.discard((idx, jdx))
                    safe.add((idx, jdx))


r, c = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(r)]

queue = deque()
v = deque()
safe = set()
wall = set()

for i in range(r):
    for j in range(c):
        if lab[i][j] == 1:
            wall.add((i, j))
        elif lab[i][j] == 2:
            v.append((i, j))
        else:
            safe.add((i, j))

ans = 0
# 이제 벽을 세우러 가볼까
for i in range(r):
    for j in range(c):
        if (i, j) in safe:
            safe.discard((i, j))
            wall.add((i, j))
            add_wall(1)
            wall.discard((i, j))
            safe.add((i, j))

print(ans)