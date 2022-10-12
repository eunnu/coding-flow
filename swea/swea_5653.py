# 가상 좌표를 이용한다.
# 주어지는 자료로 좌표화 하여 저장한다.
# 시간의 순서: 처음(비활성화) <X 시간 후> 활성화 <1 시간 후> 번식(비활성화) (번외: X 시간 후 죽음)
def grow():     # 번식하는 함수
    tmp = dict()
    for idx in cell.keys():
        y, x = idx

        if cell[idx][2] == 0:
            for direc in range(4):
                ny = y + dy[direc]
                nx = x + dx[direc]

                if (ny, nx) not in cell:
                    if (ny, nx) not in tmp:             # 기존에도 없고, 현재 번식중인데 아직 없다면 넣어주고
                        tmp[(ny, nx)] = [cell[idx][0], cell[idx][0], 1]

                    else:                               # 만일, 번식중인데 겹치는 셀이다?
                        if tmp[(ny, nx)][0] < cell[idx][0]:         # 근데 생명력이 뒷 놈이 더 강하다?
                            tmp[(ny, nx)] = [cell[idx][0], cell[idx][0], 1]               # 바꿈

        if cell[idx][1] > -1:
            cell[idx][1] -= 1
            if cell[idx][1] == 0:
                cell[idx][2] -= 1
                if cell[idx][2] == 0:
                    cell[idx][1] = cell[idx][0]
    cell.update(tmp)


for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    fir = [list(map(int, input().split())) for _ in range(N)]

    cell = dict()
    for i in range(N):
        for j in range(M):
            if fir[i][j]:
                cell[(i, j)] = [fir[i][j], fir[i][j], 1]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in cell.values():  # 1 시간씩 지남
        if i[1] > -1:
            i[1] -= 1
            if i[1] == 0:  # 1 : 비활성화 0 : 활성화
                i[2] -= 1
                if i[2] == 0:
                    i[1] = i[0]
    t = 1
    while t != K:
        grow()
        t += 1

    ans = 0
    for i in cell.values():
        if i[2] > -1:
            ans += 1

    print(f"#{tc} {ans}")




