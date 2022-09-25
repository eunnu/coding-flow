# 군집들의 리스트를 실시간으로 수와 방향을 업데이트 해준다
# 이동을 할 때의 해당 군집의 번호를 위치에 넣어준다
def check():
    for idx in range(N):
        for jdx in range(N):
            if (idx, jdx) in area:
                if len(area[(idx, jdx)]) > 1:
                    area[(idx, jdx)].sort()
                    tmp = area[(idx, jdx)]
                    for k in range(len(tmp)-1):
                        group[tmp[-1][1]][2] += group[tmp[k][1]][2]
                        group[tmp[k][1]] = [0, 0, 0, 0]


def sol(number):

    y, x, cnt, di = group[number]
    ny = y + dy[di]
    nx = x + dx[di]
    if 0 <= nx < N and 0 <= ny < N:
        if nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
            cnt //= 2
            if di % 2:
                di += 1
            else:
                di -= 1
    if cnt:
        if (ny, nx) in area:
            area[(ny, nx)] += [[cnt, number]]
        else:
            area[(ny, nx)] = [[cnt, number]]
    group[number] = [ny, nx, cnt, di]


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    group = [list(map(int, input().split())) for _ in range(K)]

    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]

    while M:
        area = dict()
        for i in range(K):
            sol(i)
        check()
        M -= 1

    ans = 0
    for i in range(K):
        ans += group[i][2]
    print(f"#{tc} {ans}")
