# 모든 조합을 구해서 BFS 돌릴 예정
from collections import deque


def bfs(a):
    global area, ans
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque()
    cpy_area = area
    active = []
    for v in range(len(a)):
        tm = a[v] + [0]
        queue.append(tm)
        active.append(a[v])

    visited = set()

    time = 0
    while queue:
        y, x, t = queue.popleft()

        if t > ans:
            break

        if cpy_area <= 0:
            break

        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]

            if 0 <= ny < N and 0 <= nx < N:
                if lab[ny][nx] == 0 and (ny, nx) not in visited:
                    cpy_area -= 1                       # 빈 공간을 줄여 나감
                    time = max(time, t+1)               # 시간을 계속 업데이트 해줌
                    visited.add((ny, nx))
                    queue.append([ny, nx, t+1])
                if lab[ny][nx] == 2 and [ny, nx] not in active and (ny, nx) not in visited:     # 비활성화 만나면 활성 시킴
                    queue.append([ny, nx, t+1])
                    visited.add((ny, nx))

    if cpy_area <= 0:                               # 빈 공간이 없어야 답을 업데이트 해줌
        ans = min(time, ans)


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

vir = []            # 바이러스 좌표 넣어주는 배열

area = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            vir.append([i, j])
        if lab[i][j] == 0:
            area += 1           # 빈 공간 개수

ans = 987654321

for i in range(1 << len(vir)):          # 조합코드로 짰다가 시간초과 떠서 부분집합으로 구현
    tmp = []
    for j in range(len(vir)):
        if i & (1 << j):
            tmp.append(vir[j])
    if len(tmp) == M:                   # 개수가 M인 경우 BFS 보냄
        bfs(tmp)

if ans == 987654321:                    # 답이 없으면 -1
    ans = -1
print(ans)

