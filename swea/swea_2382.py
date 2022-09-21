# 군집을 돌면서 이동한 인덱스를 전부 리스트에 넣어준다.
# 해당 리스트를 비워가면서 같은 인덱스 상에 존재하는 군집들을 다른 리스트에 넣어준다.
# 해당 리스트를 군집의 크기로 정렬을 한 후에 가장 큰 군집을 기준으로 모아준다.
def sol():
    for idx in range(len(group)):
        [y, x, cnt, d] = group[idx]         # 인덱스, 크기, 방향

        if cnt == 0:                           # 합쳐졌거나 사라진 군집은 넘어간다.
            continue

        ny = y + dy[d]
        nx = x + dx[d]

        if 0 < nx < N - 1 and 0 < ny < N - 1:
            move.append([ny, nx, cnt, d])
        elif nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
            if cnt//2 > 0:
                if d == 1:
                    move.append([ny, nx, cnt//2, 2])
                elif d == 2:
                    move.append([ny, nx, cnt//2, 1])
                elif d == 3:
                    move.append([ny, nx, cnt//2, 4])
                elif d == 4:
                    move.append([ny, nx, cnt//2, 3])

    group.clear()

    arr = [[0] * N for _ in range(N)]

    for jdx in range(len(move)):
        tmp = move[jdx]

        if arr[tmp[0]][tmp[1]]:
            if tmp not in comb:
                comb.append(tmp)
            if arr[tmp[0]][tmp[1]] not in comb:
                comb.append(arr[tmp[0]][tmp[1]])
        else:
            arr[tmp[0]][tmp[1]] = tmp

    if comb:
        sorted(comb, key=lambda same: same[2])
        tmp = comb.pop()
        move.remove(tmp)
        group.append(tmp)
        while comb:
            aa = comb.pop()
            move.remove(aa)
            group[-1][2] += aa[2]

    while move:
        tmp = move.pop()
        group.append(tmp)


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    group = [list(map(int, input().split())) for _ in range(K)]

    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    while M != 0:
        move = []
        comb = []
        sol()
        M -= 1

    ans = 0
    for i in range(len(group)):
        ans += group[i][2]

    print(f"#{tc} {ans}")