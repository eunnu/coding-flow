from collections import deque
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    queue = deque()
    queue.append((0, 0))

    ans = 987654321

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    dist = [[987654321] * N for _ in range(N)]
    dist[0][0] = 0

    while queue:
        y, x = queue.popleft()

        if y == N-1 and x == N-1:
            continue

        if ans < dist[y][x]:
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] < arr[y][x]:
                    cost = dist[y][x] + 1
                else:
                    cost = dist[y][x] + abs(arr[ny][nx] - arr[y][x]) + 1
                if dist[ny][nx] > cost:
                    queue.append((ny, nx))
                    dist[ny][nx] = cost

    print(f"#{tc} {dist[N-1][N-1]}")