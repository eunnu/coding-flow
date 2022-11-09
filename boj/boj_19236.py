# 일단 상어가 (0, 0)을 잡아먹는다는 거잖아?
# 그러고 물고기들이 작은 번호 순으로 이동하고 이동할 수 있는 방향으로 반시계 방향으로 회전을 한다며
# 이동을 하면서 위치를 서로 바꾸는거고?
# 그러고 상어가 물고기를 잡아먹은 방향으로 움직이면서 물고기 번호가 가장 큰 걸 찾는다?
# 물고기가 움직이고 상어가 움직인다.
from collections import deque


def fish_move():                    # 물고기 움직이십니다.
    global fish, fish_d, shark
    for num in range(17):
        if num not in fish:
            continue
        fy, fx = fish[num]
        d = fish_d[num]
        nfy, nfx = fy + dy[d], fx + dx[d]
        flag = False
        if 0 > nfy or nfy > 3 or 0 > nfx or nfx > 3 or (nfy, nfx) == shark:                 # 범위 밖이거나 상어있으면 방향 바꾸십니다.
            for _ in range(8):
                d += 1
                if d > 8:
                    d = 1
                nfy, nfx = fy + dy[d], fx + dx[d]
                if 0 <= nfy <= 3 and 0 <= nfx <= 3 and (nfy, nfx) != shark:
                    fish_d[num] = d
                    if (nfy, nfx) in fish.values():
                        for fi in fish.keys():
                            if fish[fi] == (nfy, nfx):                                      # 만약 이동할 공간에 다른 물고기 계시면
                                fish[num], fish[fi] = (nfy, nfx), (fy, fx)                  # 트레이드 하십니다.
                                flag = True
                                break
                    else:
                        fish[num] = (nfy, nfx)
                        flag = True

                if flag:
                    break

        elif 0 <= nfy <= 3 and 0 <= nfx <= 3 and (nfy, nfx) != shark:
            if (nfy, nfx) in fish.values():
                for fi in fish.keys():
                    if fish[fi] == (nfy, nfx):
                        fish[num], fish[fi] = (nfy, nfx), (fy, fx)
                        break
            else:
                fish[num] = (nfy, nfx)


fish_info = [list(map(int, input().split())) for _ in range(4)]
f_d = [0]*17
f = dict()
s = (0, 0)
s_eat = []
s_d = 0
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
queue = deque()
ans = 0
for i in range(4):
    for j in range(4):
        f_d[fish_info[i][j*2]] = fish_info[i][j*2+1]
        if i == 0 and j == 0:
            s_eat.append(fish_info[i][j*2])
            s_d = fish_info[i][j*2+1]
            continue
        f[fish_info[i][j*2]] = (i, j)
queue.append([f, f_d, s_eat, s, s_d])

while queue:
    fish, fish_d, eat, shark, shark_d = queue.popleft()                             # BFS 로 돕니다.

    # 물고기가 한 번 움직이고 상어가 그 상태에서 먹을 수 있는 경우의 수를 모두 넣어서 돌립니다.
    # 그러려면, 물고기의 이동상태에서 상어가 먹은 물고기를 제외한 물고기 정보와 상어 정보가 업데이트 되어야 합니다.

    if ans < sum(eat):
        ans = sum(eat)

    fish_move()

    sy, sx = shark

    while True:
        number = 0
        nsy, nsx = sy + dy[shark_d], sx + dx[shark_d]
        if (nsy, nsx) in fish.values():                         # 만약 물고기가 있다면
            for i in fish.keys():                               # 물고기를 먹고 상어가 그 자리를 꿰차고 방향도 바뀌어야 함
                if fish[i] == (nsy, nsx):
                    clone_fish = fish.copy()
                    f_md = [i for i in fish_d]
                    clone_fish.pop(i)
                    queue.append([clone_fish, f_md, eat + [i], (nsy, nsx), f_md[i]])
                    break

        elif 0 > nsx or 0 > nsy or nsx > 3 or nsy > 3:         # 상어가 집으로 돌아갈 조건
            break

        sy, sx = nsy, nsx                                      # 더 먹을 수 있다면 움직이여야지

print(ans)


# 7 1 2 6 15 7 9 3
# 3 5 1 4 14 1 10 6
# 6 4 13 3 4 6 11 1
# 16 5 8 7 5 2 12 2
#
# 답7
#
# 7 6 2 6 15 7 9 3
# 3 5 1 4 14 1 10 6
# 6 4 13 3 4 6 11 1
# 16 5 8 7 5 2 12 2
#
# 답 88
#
# 7 6 2 1 15 1 9 1
# 3 1 1 1 14 7 10 3
# 6 1 13 6 4 3 11 4
# 16 3 8 7 5 2 12 2
#
# 답 42
#
# 12 6 14 5 4 5 6 7
# 15 1 11 3 3 7 7 5
# 10 3 8 2 16 6 1 1
# 5 8 2 7 13 6 9 4
#
# 답 55 또는 76
