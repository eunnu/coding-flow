T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = []
    end = []
    queue = []

    for i in range(N):
        maze.append(list(map(int, list(input()))))
        for j in range(N):
            if maze[i][j] == 2:
                queue.append([i, j, 0])
            elif maze[i][j] == 3:
                end.append([i, j])

    visit = set()
    ans = 0
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    while queue:
        [y, x, cnt] = queue.pop(0)

        visit.add((y, x))

        if end[0] == [y, x]:
            ans = cnt - 1
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or (ny, nx) in visit or maze[ny][nx] == 1:
                continue

            queue.append([ny, nx, cnt + 1])

    print(f"#{tc} {ans}")