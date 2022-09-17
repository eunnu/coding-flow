# 소요시간 : 1시간 20분


def bfs(y, x, t):
    global direc

    if t == L:
        return

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        # 파이프가 연결이 되어 있는지, 갈 수 있는 방향인지 확인해 주기 위함
        if idx == 0:        # 상
            direc = 1       # 하로
        elif idx == 1:      # 하
            direc = 0       # 상으로
        elif idx == 2:      # 좌
            direc = 3       # 우로
        else:               # 우
            direc = 2       # 좌로

        if 0 <= nx < M and 0 <= ny < N:
            # 지금 위치에서 진행하려는 방향이 파이프로 연결이 되어 있는지 확인
            if move[load[y][x]][idx] == 1 and move[load[ny][nx]][direc] == 1:
                # 방문한 적이 없거나 이전에 방문 한 적이 있다면 전 보다 늦은 시간에 방문을 했어야 한다.
                # 이 조건이 없으면 시간 초과가 뜸
                if not visited[ny][nx] or (visited[ny][nx] > visited[y][x] + 1):
                    visited[ny][nx] = t + 1
                    bfs(ny, nx, t + 1)


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    load = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*M for _ in range(N)]

    move = [[0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 1, 1, 0],
            [1, 0, 1, 0]]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[R][C] = 1

    direc = 0
    bfs(R, C, 1)

    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                ans += 1

    print(f"#{tc} {ans}")