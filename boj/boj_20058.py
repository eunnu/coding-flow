# 일단 배열을 나누어서 회전 시키고
# 얼음끼리 인접한 칸이 3개 이상인지 확인하고
# 미만이라면 1씩 빼주고
def dfs():              # 가장 큰 덩어리를 찾아주는 dfs 함수
    cnt = 0
    global ans
    while stack:
        r, c = stack.pop()
        for direct in range(4):
            nr = r + dy[direct]
            nc = c + dx[direct]

            if 0 <= nr < 2**N and 0 <= nc < 2**N:
                if shark[nr][nc] > 0 and (nr, nc) not in visit:
                    cnt += 1
                    stack.append((nr, nc))
                    visit.add((nr, nc))

    ans = max(ans, cnt)


def ice():              # 얼음을 녹이는 함수
    melt = []
    for ii in range(2**N):
        for jj in range(2**N):
            cnt = 0
            for direc in range(4):
                ni = ii + dy[direc]
                nj = jj + dx[direc]

                if 0 <= ni < 2**N and 0 <= nj < 2**N:
                    if shark[ni][nj] > 0:
                        cnt += 1

            if cnt < 3:
                if shark[ii][jj]:
                    melt.append((ii, jj))
                    # 굳이 새로운 리스트에 좌표를 넣어주는 이유는 녹은 얼음이 다른 얼음에 영향을 미치는 것을 막기 위함

    while melt:     # 얼음을 녹여줌
        yy, xx = melt.pop()
        shark[yy][xx] -= 1


def turn(num):      # 90도 회전하는 함수
    ldx = 2**num    # 격자 크기
    for jdx in range(0, 2**N - ldx + 1, ldx):       # y축 기준
        for idx in range(0, 2**N - ldx + 1, ldx):   # x축 기준
            x = jdx
            y = j_idx = idx
            i_idx = jdx + ldx - 1
            while True:                             # 모든 격자를 다 회전 시켜 주기 위한 반복문
                tmp[x][y] = shark[i_idx][j_idx]
                if x == jdx + ldx - 1 and y == idx + ldx - 1:
                    break

                y += 1
                i_idx -= 1

                if y == idx + ldx:
                    x += 1
                    if x == idx:
                        x = jdx
                    y = idx

                if i_idx == jdx - 1:
                    i_idx = jdx + ldx - 1
                    j_idx += 1
                    if j_idx == idx + ldx:
                        j_idx = idx

    for idx in range(2**N):             # 회전시킨 배열을 원래 배열로 바꾸는 반복문
        for jdx in range(2**N):
            shark[idx][jdx] = tmp[idx][jdx]


N, Q = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))
ans = 0
total = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for magic in range(Q):
    tmp = [[0]*(2**N) for _ in range(2**N)]
    ans = 0
    turn(L[magic])
    ice()

visit = set()
for i in range(2**N):
    total += sum(shark[i])
    for j in range(2**N):
        if (i, j) not in visit:
            stack = [(i, j)]
            dfs()

print(total)
print(ans)

