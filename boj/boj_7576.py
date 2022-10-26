# 그냥 BFS 풀 생각임
from collections import deque


N, M = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque()

for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            queue.append((0, i, j))

visit = set()
ans = []
while queue:
    day, y, x = queue.popleft()
    visit.add((y, x))
    ans.append(day)
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < M and 0 <= nx < N:
            if tomato[ny][nx] == 0:
                tomato[ny][nx] = day + 1
                if (ny, nx) not in visit:
                    queue.append((day+1, ny, nx))

for i in range(M):
    if 0 in tomato[i]:
        ans.clear()
        ans.append(-1)
        break
else:
    ans.sort()
print(ans[-1])

