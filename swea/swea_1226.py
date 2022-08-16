T = 10

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    tc = int(input())

    maze = []

    sx, sy, ex, ey = 0, 0, 0, 0
    for i in range(16):
        maze.append(list(map(int, input())))
        for j in range(16):
            if maze[i][j] == 2:
               sx, sy = j, i
            elif maze[i][j] == 3:
                ex, ey = j, i

    visited = [[0]*16 for _ in range(16)]

    stack = []
    stack.append([sy, sx])

    ans = 0
    while stack:
        a = stack.pop()
        x, y = a[1], a[0]

        if x == ex and y == ey:
            ans = 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > 15 or ny > 15 or visited[ny][nx] or maze[ny][nx] == 1:
                continue

            stack.append([ny, nx])
            visited[ny][nx] = 1

    print(f"#{tc} {ans}")