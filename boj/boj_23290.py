# 물고기 이동 -> 상어가 움직임 -> 물고기 복제
# 상,좌,하,우 (사전 순서)
# 물고기는 반시계방향으로 45도씩 회전
# 물고기가 사라져도 냄새는 2회 남는다.
# 물고기들은 물고기 냄새가 남아있거나 상어가 있으면 그 방향으로는 이동할 수 없다.
# 물고기는 이동을 안할 수도 있다.
# 물고기는 (뚠뚠) 오늘도 (뚠뚠) 열심히~ 수영~ 하네(뚠뚠)
# 상어는 (뚠뚠) 오늘도 (뚠뚠) 열심히 잡아 먹네~(뚠뚠)
# 응애 상어 (뚜루루루루) 바다속 (뚜루루루루) 응애 상어!!
def smell_check():
    global smell
    no_smell = []
    for smell_index in smell.keys():
        if smell[smell_index] > 2:
            no_smell.append(smell_index)
        else:
            smell[smell_index] += 1

    for no_s in no_smell:
        smell.pop(no_s)


def shark_move():           # 상어 이동
    global fish, dd
    many = []
    maxi = 0
    for idx in range(4):
        ony = shark[0] + sdy[idx]
        onx = shark[1] + sdx[idx]
        o_cnt = 0
        eat = set()
        if 1 <= ony <= 4 and 1 <= onx <= 4:
            if (ony, onx) in fish:
                o_cnt += len(fish[(ony, onx)])
                eat.add((ony, onx))
            for jdx in range(4):
                tny = ony + sdy[jdx]
                tnx = onx + sdx[jdx]
                t_cnt = o_cnt
                if 1 <= tny <= 4 and 1 <= tnx <= 4:
                    if (tny, tnx) in fish and (tny, tnx) not in eat:
                        t_cnt += len(fish[(tny, tnx)])
                        eat.add((tny, tnx))
                    for kdx in range(4):
                        ny = tny + sdy[kdx]
                        nx = tnx + sdx[kdx]
                        cnt = t_cnt
                        if 1 <= ny <= 4 and 1 <= nx <= 4:
                            if (ny, nx) in fish and (ny, nx) not in eat:
                                cnt += len(fish[(ny, nx)])

                        if maxi < cnt:
                            maxi = cnt
                            many = [idx, jdx, kdx]
                        if dd == 3 and idx == 3:
                            print(idx, jdx, kdx, cnt)
                if (tny, tnx) in eat:
                    eat.discard((tny, tnx))
            if (ony, onx) in eat:
                eat.discard((ony, onx))

    for ms in many:
        ny = shark[0] + sdy[ms]
        nx = shark[1] + sdx[ms]
        if (ny, nx) in fish:
            fish.pop((ny, nx))
            smell[(ny, nx)] = 0

        shark[0] = ny
        shark[1] = nx


def fish_move():           # 물고기 이동
    global fish, clone_fish
    move_fish = dict()
    for fi in fish.keys():
        if fi not in clone_fish:
            clone_fish[fi] = []
        for jdx in range(len(fish[fi])):
            clone_fish[fi].append(fish[fi][jdx])
            dire = fish[fi][jdx]
            for _ in range(8):
                fny = fi[0] + fdy[dire]
                fnx = fi[1] + fdx[dire]

                if 1 <= fny <= 4 and 1 <= fnx <= 4:
                    if (fny, fnx) not in smell and shark != [fny, fnx]:
                        if (fny, fnx) not in move_fish:
                            move_fish[(fny, fnx)] = []
                        move_fish[(fny, fnx)].append(dire)
                        break
                dire -= 1
                if dire < 1:
                    dire = 8

    fish = move_fish


M, S = map(int, input().split())
fish = dict()
smell = dict()
for _ in range(M):
    i, j, d = map(int, input().split())
    if (i, j) not in fish:
        fish[(i, j)] = []
    fish[(i, j)].append(d)

shark = list(map(int, input().split()))
fdy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
fdx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
sdy = [-1, 0, 1, 0]
sdx = [0, -1, 0, 1]

for dd in range(S):
    clone_fish = dict()
    fish_move()
    shark_move()
    smell_check()
    for f in clone_fish.keys():
        if f not in fish:
            fish[f] = clone_fish[f]
        else:
            for j in clone_fish[f]:
                fish[f].append(j)

ans = 0
for i in fish.keys():
    ans += len(fish[i])

print(smell)
print(shark)
print(ans)