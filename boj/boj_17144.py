def air():
    global top, bottom

    cpy = [[0]*C for _ in range(R)]
    for dt in dust.keys():
        if dt[0] == 0 and 0 < dt[1] <= C-1:
            cpy[dt[0]][dt[1] - 1] = dust[dt]
        elif dt[0] == top and 0 <= dt[1] < C-1:
            cpy[dt[0]][dt[1] + 1] = dust[dt]
        elif dt[0] == bottom and 0 <= dt[1] < C-1:
            cpy[dt[0]][dt[1] + 1] = dust[dt]
        elif dt[0] == R-1 and 0 < dt[1] <= C-1:
            cpy[dt[0]][dt[1] - 1] = dust[dt]
        elif dt[1] == 0 and 0 <= dt[0] < top:
            cpy[dt[0]+1][dt[1]] = dust[dt]
        elif dt[1] == 0 and bottom < dt[0] <= R-1:
            cpy[dt[0]-1][dt[1]] = dust[dt]
        elif dt[1] == C-1 and 0 < dt[0] <= top:
            cpy[dt[0]-1][dt[1]] = dust[dt]
        elif dt[1] == C-1 and bottom <= dt[0] < R-1:
            cpy[dt[0]+1][dt[1]] = dust[dt]
        elif dt == (0, 0):
            cpy[1][0] = dust[dt]
        elif dt == (bottom, C-1):
            cpy[bottom+1][C-1] = dust[dt]
        else:
            cpy[dt[0]][dt[1]] = dust[dt]
    cpy[top][0] = cpy[bottom][0] = 0
    return cpy


def sp():
    move = dict()

    for ii in range(R):
        for jj in range(C):
            if li[ii][jj] > 0:
                cnt = 0
                for di in range(4):
                    ny = ii + dy[di]
                    nx = jj + dx[di]

                    if 0 <= ny < R and 0 <= nx < C:
                        if (ny, nx) != (top, 0) and (ny, nx) != (bottom, 0):
                            cnt += 1
                            if (ny, nx) in move:
                                move[(ny, nx)] += li[ii][jj] // 5
                            else:
                                move[(ny, nx)] = li[ii][jj] // 5

                if (ii, jj) in move:
                    move[(ii, jj)] += li[ii][jj] - li[ii][jj] // 5 * cnt
                else:
                    move[(ii, jj)] = li[ii][jj] - li[ii][jj] // 5 * cnt

    return move


R, C, T = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(R)]

top = tuple()
bottom = tuple()
dust = dict()

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

for i in range(R):
    if li[i][0] == -1:
        top = i
        bottom = i+1
        break

for _ in range(T):
    # 먼지가 흩어지는 함수로
    dust = sp()
    li = air()

ans = 0
for i in range(R):
    ans += sum(li[i])

print(ans)