# 배추 구역이 몇 군데인지
def check():
    while stack:
        y, x = stack.pop()

        for direc in range(4):
            ny = y + dy[direc]
            nx = x + dx[direc]

            if 0 <= nx < M and 0 <= ny < N:
                if ground[ny][nx] and (ny, nx) not in visit:
                    visit.add((ny, nx))
                    stack.append((ny, nx))


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    ground = [[0]*M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())
        ground[r][c] = 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visit = set()

    ans = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] and (i, j) not in visit:
                visit.add((i, j))
                stack = [(i, j)]
                check()
                ans += 1

    print(ans)
