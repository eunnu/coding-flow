# 상어가 냄새를 뿌리고
# 1초마다 인접한 칸으로 이동 -> 냄새를 뿌림 -> K번 이동 후 사라짐
# 인접한 칸을 고를 때는 냄새가 없어야 함
# 이동 한 후 여러마리가 한 칸에 있으면 번호가 가장 작은 상어만 남음
# 각 상어마다 방향 우선순위가 주어진다.
# 상, 하, 좌, 우
# 이동 할 수 있는 곳이 냄새를 뿌린곳이라면, 우선순위로 돌 때, 냄새가 있는 곳이 있으면 저장해 놓는다.
from pprint import pprint


def smelling():
    for idx in range(N):
        for jdx in range(N):
            if sea[idx][jdx]:
                smell[(idx, jdx)] = [K, sea[idx][jdx]]


def move():
    # 빈 곳이 있다면 우선순위 순으로
    # 빈 곳이 없다면 우선순위 순에서 본인의 냄새가 있는 곳으로
    # 이동하면서 상어 방향 바꿔주고, 바다 배열 바꿔주어야 함
    # 여러군데에 존재 할 수 있으니 딕셔너리에 좌표와 상어 번호를 넣어주고, 1마리면 그냥 저장해주고 아니면 가장 작은 번호를 넣어준다.
    # 그 가장 작은 번호를 제외하고는 s에서 해당 번호들을 제외해 준다.
    move_shark = [[0]*N for _ in range(N)]
    alive = []
    for r in range(N):
        for c in range(N):
            if sea[r][c]:
                num = sea[r][c]
                d = shark[num][di[num]]
                sel = 0

                for kdx in range(4):
                    ny = r + dy[d[kdx]]
                    nx = c + dx[d[kdx]]
                    if 0 <= ny < N and 0 <= nx < N:

                        if (ny, nx) in smell and smell[(ny, nx)][1] == num and sel == 0:
                            sel = d[kdx]

                        if sea[ny][nx] == 0 and (ny, nx) not in smell:
                            if move_shark[ny][nx] == 0 or (move_shark[ny][nx] != 0 and move_shark[ny][nx] > num):
                                move_shark[ny][nx] = num
                                di[num] = d[kdx]
                                sel = 0
                                break
                            elif move_shark[ny][nx] != 0 and move_shark[ny][nx] < num:
                                sel = 0
                                break

                if sel != 0:
                    ny = r + dy[sel]
                    nx = c + dx[sel]
                    if move_shark[ny][nx] == 0 or move_shark[ny][nx] > num:
                        move_shark[ny][nx] = num
                        di[num] = sel

    for r in range(N):
        for c in range(N):
            sea[r][c] = move_shark[r][c]
            if move_shark[r][c]:
                alive.append(move_shark[r][c])

    s.clear()
    for r in alive:
        s.append(r)


def low_smell():
    die = []
    for sm in smell.keys():
        smell[sm][0] -= 1
        if smell[sm][0] < 1:
            die.append(sm)

    for d in die:
        smell.pop(d)


N, M, K = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
di = [0] + list(map(int, input().split()))

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

shark = [dict()]
for i in range(M):
    tmp = dict()
    for j in range(1, 5):
        tmp[j] = list(map(int, input().split()))

    shark.append(tmp)

smell = dict()
ans = 0
s = [i for i in range(1, M+1)]

while len(s) > 1:
    smelling()
    ans += 1
    move()
    low_smell()
    if ans > 1000:
        ans = -1
        break

print(ans)

