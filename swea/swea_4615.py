# 돌을 두면 그 돌의 인덱스를 중심으로 다른 돌이 있는 위치들을 찾아서 전달
# 그 반대 방향으로 계속 진행하면서 다른 돌이 있는지 확인
# 만약 돌이 없다면 반환, 돌이 있으면 바꿔줌
def check(y, x, d, direc):

    visited = [[y, x]]
    flag = True
    while flag:
        ny = y + dy[direc]
        nx = x + dx[direc]

        if 0 < ny <= N and 0 < nx <= N:
            if arr[ny][nx] == d:
                flag = False

            elif not arr[ny][nx]:
                return

            elif arr[ny][nx] and arr[ny][nx] != d:
                visited.append([ny, nx])
        else:
            return

        y, x = ny, nx

    if visited:
        while visited:
            [y, x] = visited.pop()
            arr[y][x] = d


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0] * (N+1) for _ in range(N+1)]
    arr[N//2][N//2], arr[N//2+1][N//2+1] = 2, 2
    arr[N//2 + 1][N//2], arr[N//2][N//2 + 1] = 1, 1

    # 왼, 위, 위왼, 아래왼, 위오, 아래오, 아래, 오
    dy = [0, -1, -1, 1, -1, 1, 1, 0]
    dx = [-1, 0, -1, -1, 1, 1, 0, 1]
    for _ in range(M):
        r, c, dol = map(int, input().split())
        arr[r][c] = dol
        for i in range(8):
            nr = r + dy[i]
            nc = c + dx[i]
            if 0 < nr <= N and 0 < nc <= N:
                if arr[nr][nc] != dol and arr[nr][nc] != 0:
                    check(nr, nc, dol, i)

    black, white = 0, 0
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print(f"#{tc} {black} {white}")