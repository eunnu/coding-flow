# 시간 복잡도 : 500 * 500 * 256 = 대략 1억번 => 1초에 근사함
# 브루트 포스 알고리즘

import sys

N, M, B = map(int, sys.stdin.readline().split(" "))
res_t, res_h = 987654321, 0
mine = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

for i in range(257):  # 최대 높이가 256
    height, t_time = i, 0
    block = B
    for y in range(N):
        for x in range(M):
            if mine[y][x] > i:
                t_time += (mine[y][x] - i) * 2
                block += mine[y][x] - i
            elif mine[y][x] < i:
                t_time += (i - mine[y][x])
                block -= (i - mine[y][x])
    if block < 0:
        break

    if res_t >= t_time:
        res_t = t_time
        if res_h < height:
            res_h = height

print(res_t, res_h)