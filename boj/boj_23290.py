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
        if smell[smell_index] == 0:
            no_smell.append(smell_index)
        else:
            smell[smell_index] -= 1

    for no_s in no_smell:
        smell.pop(no_s)


def shark_move():           # 상어 이동
    global fish, shark, dd

    many = []
    maxi = -1

    for first_move in range(4):
        first_y = shark[0] + sdy[first_move]
        first_x = shark[1] + sdx[first_move]

        eat = set()
        first_eat = 0
        if 1 <= first_x <= 4 and 1 <= first_y <= 4:
            if (first_y, first_x) in fish:
                first_eat = len(fish[(first_y, first_x)])
                eat.add((first_y, first_x))

            for second_move in range(4):
                second_y = first_y + sdy[second_move]
                second_x = first_x + sdx[second_move]

                if 1 <= second_x <= 4 and 1 <= second_y <= 4:
                    second_eat = first_eat
                    if (second_y, second_x) in fish:
                        if (second_y, second_x) not in eat:
                            second_eat = first_eat + len(fish[(second_y, second_x)])
                            eat.add((second_y, second_x))

                    for third_move in range(4):
                        ny = second_y + sdy[third_move]
                        nx = second_x + sdx[third_move]

                        if 1 <= ny <= 4 and 1 <= nx <= 4:
                            if maxi < second_eat:
                                maxi = second_eat
                                many = [(first_y, first_x), (second_y, second_x), (ny, nx)]

                            if (ny, nx) in fish:
                                if (ny, nx) not in eat:
                                    if maxi < second_eat + len(fish[(ny, nx)]):
                                        maxi = second_eat + len(fish[(ny, nx)])
                                        many = [(first_y, first_x), (second_y, second_x), (ny, nx)]

                    if (second_y, second_x) in eat:
                        eat.discard((second_y, second_x))

    for shark_eat in many:
        if shark_eat in fish:
            fish.pop(shark_eat)
            smell[shark_eat] = 2

    shark = many[-1]

    smell_check()


def fish_move():           # 물고기 이동
    global fish
    clone_fish = dict()
    move_fish = dict()
    for fi in fish.keys():
        clone_fish[fi] = fish[fi]
        for jdx in range(len(fish[fi])):
            dire = fish[fi][jdx]
            flag = False
            for _ in range(8):
                fny = fi[0] + fdy[dire]
                fnx = fi[1] + fdx[dire]

                if 1 <= fny <= 4 and 1 <= fnx <= 4:
                    if (fny, fnx) not in smell and shark != (fny, fnx):
                        if (fny, fnx) not in move_fish:
                            move_fish[(fny, fnx)] = []
                        move_fish[(fny, fnx)].append(dire)
                        flag = True
                        break
                dire -= 1
                if dire < 1:
                    dire = 8

            if not flag:
                if (fi[0], fi[1]) not in move_fish:
                    move_fish[(fi[0], fi[1])] = []
                move_fish[(fi[0], fi[1])].append(fish[fi][jdx])

    fish = move_fish

    shark_move()

    for f in clone_fish.keys():
        if f not in fish:
            fish[f] = clone_fish[f]
        else:
            fish[f] += clone_fish[f]


M, S = map(int, input().split())
fish = dict()
smell = dict()
for _ in range(M):
    i, j, d = map(int, input().split())
    if (i, j) not in fish:
        fish[(i, j)] = []
    fish[(i, j)].append(d)

shark = tuple(map(int, input().split()))
fdy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
fdx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
sdy = [-1, 0, 1, 0]
sdx = [0, -1, 0, 1]

for dd in range(S):
    fish_move()

ans = 0
for i in fish.keys():
    ans += len(fish[i])

print(ans)