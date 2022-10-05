def sol():
    while stack:
        ny, nx = stack.pop()

        for direc in range(8):
            y = ny + dy[direc]
            x = nx + dx[direc]

            if 0 <= y < h and 0 <= x < w:
                if not visit[y][x]:
                    if li[y][x]:
                        stack.append((y, x))
                        visit[y][x] = 1


while True:
    w, h = map(int, input().split())
    if not w and (not h):
        break

    li = [list(map(int, input().split())) for _ in range(h)]

    ans = 0

    dy = [-1, 1, 0, 0, 1, 1, -1, -1]
    dx = [0, 0, -1, 1, -1, 1, 1, -1]

    visit = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if li[i][j] and not visit[i][j]:
                stack = [(i, j)]
                visit[i][j] = 1
                sol()
                ans += 1

    print(ans)
