from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    load = [[987654321] * N for _ in range(N)]
    queue = deque()
    queue.append([0, 0])
    visited = set()

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        [y, x] = queue.popleft()

        visited.add((y, x))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if (ny, nx) not in visited:
                    load[ny][nx] = min(load[ny][nx], li[y][x] + abs(li[ny][nx] - li[y][x]) + 1)
                    if [ny, nx] not in queue:
                        queue.append([ny, nx])

    print(load)
    print(f"#{tc} {load[N-1][N-1]}")