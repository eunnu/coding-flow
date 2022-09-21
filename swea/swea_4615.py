def game(y, x, dol_1):
    for direc in range(8):
        nr = y + dy[direc]
        nc = x + dx[direc]
        check = False
        if 0 < nc <= N and 0 < nr <= N:
            if area[nr][nc] == dol_1:
                flag = True
                cnt = 1
                visited = [[nr, nc]]
                while flag:
                    fr = nr + dy[7 - direc]
                    fc = nc + dx[7 - direc]
                    if 0 < fc <= N and 0 < fr <= N:
                        if area[fr][fc] != 0 and area[fr][fc] == dol_1:
                            for k in visited:
                                area[k[0]][k[1]] = dol_1
                            if dol_1 == 1:
                                d[1], d[2] = d[1] + cnt, d[2] - cnt
                                check = True
                                flag = False
                            else:
                                d[1], d[2] = d[1] - cnt, d[2] + cnt
                                check = True
                                flag = False
                        elif area[fr][fc] != 0 and area[fr][fc] != dol_1:
                            visited.append([fr, fc])
                            cnt += 1
                        elif area[fr][fc] == 0:
                            break
                        nr, nc = fr, fc
        if check:
            break


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [[0]*(N+1) for _ in range(N+1)]
    area[N//2][N//2], area[N//2+1][N//2+1] = 2, 2
    area[N//2+1][N//2], area[N//2][N//2+1] = 1, 1

    d = [0, 2, 2]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(M):
        print(area)
        r, c, dol = map(int, input().split())
        area[r][c] = dol
        for j in range(8):
            ny = r + dy[j]
            nx = c + dx[j]

            if 0 < nx <= N and 0 < ny <= N:
                if area[ny][nx] != 0 and area[ny][nx] != dol:
                    game(ny, nx, dol)

    print(f"#{tc} {d[1]} {d[2]}")