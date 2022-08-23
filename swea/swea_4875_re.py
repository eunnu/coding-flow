def miro(y, x):
    global ans

    if [y, x] not in visit:
        visit.append([y, x])

    for idx in range(4):
        ny = y + dy[idx]
        nx = x + dx[idx]

        if maze[ny][nx] == '2':
            ans = 1
        return

        if ny < 0 or nx < 0 or ny >= N or nx >= N or [ny, nx] in visit or maze[ny][nx] == '1':
            continue

        miro(ny, nx)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ans = 0
    maze = []
    start_y, start_x = 0, 0
    for i in range(N):
        maze.append(input())
        for j in range(N):
            if maze[i][j] == '3':
                start_x, start_y = j, i

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visit = []
    miro(start_y, start_x)

    print(f"#{tc} {ans}")