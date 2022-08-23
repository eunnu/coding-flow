T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = []
    stack = []
    for i in range(N):
        maze.append(input())
        for j in range(N):
            if maze[i][j] == '2':
                stack.append([i, j])

    visit = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans = 0
    while stack:
        front = stack.pop()
        x = front[1]
        y = front[0]

        if front not in visit:
            visit.append(front)

        if maze[y][x] == '3':
            ans = 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or [ny, nx] in visit or maze[ny][nx] == '1':
                continue

            stack.append([ny, nx])

    print(f"#{tc} {ans}")