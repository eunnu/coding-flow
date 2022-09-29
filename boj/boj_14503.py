N, M = map(int, input().split())
a, b, direction = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

queue = [[a, b, direction]]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

ans = 0
while queue:
    y, x, d = queue.pop()

    ny = y + dy[d]
    nx = x + dx[d]

    if not room[y][x]:
        room[y][x] = 2
        ans += 1

    for _ in range(4):
        d -= 1
        if d < 0:
            d = 3
        if 0 <= y+dy[d] < N and 0 <= x+dx[d] < M:
            if not room[y+dy[d]][x+dx[d]]:
                queue.append([y+dy[d], x+dx[d], d])
                break

    else:
        y -= dy[d]
        x -= dx[d]
        if 0 <= x < M and 0 <= y < N:
            if room[y][x] != 1:
                queue.append([y, x, d])
            else:
                break
print(ans)