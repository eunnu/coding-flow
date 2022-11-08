# 일단 상어가 (0, 0)을 잡아먹는다는 거잖아?
# 그러고 물고기들이 작은 번호 순으로 이동하고 이동할 수 있는 방향으로 반시계 방향으로 회전을 한다며
# 이동을 하면서 위치를 서로 바꾸는거고?
# 그러고 상어가 물고기를 잡아먹은 방향으로 움직이면서 물고기 번호가 가장 큰 걸 찾는다?
# 물고기가 움직이고 상어가 움직인다.
from collections import deque


def fish_move(fm, x):
    for num in range(17):
        if num not in fm:
            continue
        fy, fx = fm[num]
        d = fish_d[num]
        nfy, nfx = fy + dy[d], fx + dx[d]
        flag = False
        if 0 > nfy or nfy > 3 or 0 > nfx or nfx > 3 or (nfy, nfx) == x:
            for _ in range(8):
                d += 1
                if d > 8:
                    d = 1
                nfy, nfx = fy + dy[d], fx + dx[d]
                if 0 <= nfy <= 3 and 0 <= nfx <= 3 and (nfy, nfx) != x:
                    fish_d[num] = d
                    if (nfy, nfx) in fm.values():
                        for fi in fm.keys():
                            if fm[fi] == (nfy, nfx):
                                fm[num], fm[fi] = (nfy, nfx), (fy, fx)
                                flag = True
                                break
                    else:
                        fm[num] = (nfy, nfx)
                        flag = True

                if flag:
                    break
        elif 0 <= nfy <= 3 and 0 <= nfx <= 3 and (nfy, nfx) != x:
            if (nfy, nfx) in fm.values():
                for fi in fm.keys():
                    if fm[fi] == (nfy, nfx):
                        fm[num], fm[fi] = (nfy, nfx), (fy, fx)
                        break
            else:
                fm[num] = (nfy, nfx)
    return fm


fish_info = [list(map(int, input().split())) for _ in range(4)]
fish_d = [0]*17
f = dict()
s = (0, 0)
s_eat = 0
s_d = 0
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
queue = deque()
ans = 0
for i in range(4):
    for j in range(4):
        fish_d[fish_info[i][j*2]] = fish_info[i][j*2+1]
        if i == 0 and j == 0:
            s_eat = fish_info[i][j*2]
            s_d = fish_info[i][j*2+1]
            continue
        f[fish_info[i][j*2]] = (i, j)
queue.append([f, s_eat, s, s_d])

while queue:
    fish, eat, shark, shark_d = queue.popleft()
    if ans < eat:
        ans = eat
    f_m = fish_move(fish, shark)
    sy, sx = shark
    while True:
        number = 0
        nsy, nsx = sy + dy[shark_d], sx + dx[shark_d]
        if 0 > nsy or 0 > nsx or 3 < nsx or 3 < nsy or (nsy, nsx) not in f_m.values():
            break
        if (nsy, nsx) in f_m.values():
            for i in f_m.keys():
                if f_m[i] == (nsy, nsx):
                    number = i
                    break

            idx = f_m[number]
            clone_fish = f_m.copy()
            clone_fish.pop(number)
            queue.append([clone_fish, eat + number, idx, fish_d[number]])

        sy, sx = nsy, nsx

print(ans)