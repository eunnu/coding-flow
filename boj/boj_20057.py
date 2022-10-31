# 일단 문제 그대로 풀어보겠습니다.
# append_left 해주어서 달팽이 역순으로 넣어주고
# 좌표를 넣어주는 것이 아닌 방향을 넣어줄 것
# x 가 아니라 y 의 양으로 하는 것..
from collections import deque


def snail_d():              # 달팽이 구현해서 방향을 넣어 줌
    r, c, di = 0, 0, 2
    while True:
        sr = r + sy[di]
        sc = c + sx[di]

        if sr == N//2 and sc == N//2:
            break

        if 0 <= sr < N and 0 <= sc < N:
            if arr[sr][sc] < 0:
                snail.append(abs(3-di))         # 달팽이랑 반대 방향이기 때문에
                arr[sr][sc] = abs(3-di)
                r = sr
                c = sc
            else:
                di += 1
                di %= 4
        else:
            di += 1
            di %= 4


def cane(y, x, d, sd):                       # 넘겨 받은 방향과 모래 양으로 모래를 노나줌
    global ans
    tmp = 0
    for idx in range(10):
        if idx == 9:                         # 마지막 남은 양을 넘겨 줄때
            ny = y + dy[d][idx]
            nx = x + dx[d][idx]

            if 0 <= ny < N and 0 <= nx < N:
                ton[ny][nx] += sd - tmp
            else:
                ans += sd - tmp

            break
        plus = int(sand[idx]*sd)
        tmp += plus                         # 노나 준 모래 양을 더해 놨다가 마지막에 전체 양에서 제외해야함
        ny = y + dy[d][idx]
        nx = x + dx[d][idx]

        if 0 <= ny < N and 0 <= nx < N:     # 격자 내냐
            ton[ny][nx] += plus
        else:                               # 격자 밖이냐
            ans += plus


N = int(input())
ton = [list(map(int, input().split())) for _ in range(N)]

sand = [0.01, 0.01, 0.02, 0.02, 0.05, 0.07, 0.07, 0.1, 0.1, 1]

dy = [[1, 1, 0, 0, -2, 0, 0, -1, -1, -1],               # 상좌우하 1퍼~ 오름차순
      [-1, 1, -2, 2, 0, -1, 1, -1, 1, 0],
      [-1, 1, -2, 2, 0, -1, 1, -1, 1, 0],
      [-1, -1, 0, 0, 2, 0, 0, 1, 1, 1]]

dx = [[-1, 1, -2, 2, 0, -1, 1, -1, 1, 0],
      [1, 1, 0, 0, -2, 0, 0, -1, -1, -1],
      [-1, -1, 0, 0, 2, 0, 0, 1, 1, 1],
      [-1, 1, -2, 2, 0, -1, 1, -1, 1, 0]]

sy = [-1, 0, 0, 1]
sx = [0, -1, 1, 0]

arr = [[-1]*N for _ in range(N)]
snail = deque()
arr[0][0] = 1
snail_d()
snail.append(1)

i = j = N//2
ans = 0
flag = True
while snail:
    direc = snail.pop()

    i += sy[direc]
    j += sx[direc]

    if ton[i][j] == 0:
        continue
    s = ton[i][j]
    if 0 <= i < N and 0 <= j < N:
        cane(i, j, direc, s)
    else:
        ans += s
    ton[i][j] = 0

print(ans)