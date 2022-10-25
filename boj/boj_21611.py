# 달팽이 모양으로 리스트에 좌표를 순서대로 넣어준다.
# 방향으로 돌이 던져 지면 해당 좌표에서 좌우, 상하로 퍼지면서 이웃하는 돌의 크기를 확인해준다.
# 달팽이 모양 좌표 리스트를 역으로 돌면서 값이 존재하면 그 값들을 넣어준다.
# 기존 배열에서 달팽이 리스트를 역으로 다시 값 들을 초기화 시켜준다.
# 달팽이 리스트를 역으로 돌면서 연속되는 숫자가 4개 이상인 부분들을 지워준다.
# 없으면 종료
# 그룹별로 구슬을 퍼뜨려 준다.
def change_ball():          # 구슬 퍼뜨려 주는 함수
    group_ball = []
    num = shark[snail[-1][0]][snail[-1][1]]         # 처음 비교해 줄 구슬 번호와 개수
    cnt_g = 1
    for sdx in range(len(snail)-2, -1, -1):
        r, c = snail[sdx]
        if num == shark[r][c]:                      # 번호가 같다면 개수를 더해주고
            cnt_g += 1

        else:                                       # 번호가 다르다면 개수와, 번호를 순서대로 넣어준다.
            group_ball.append(cnt_g)
            group_ball.append(num)
            cnt_g = 1                               # 번호와 개수를 초기화 시켜줌
            num = shark[r][c]

    t = 0
    for sdx in range(len(snail)-1, -1, -1):
        r, c = snail[sdx]
        if t < len(group_ball):                     # 그룹 길이보다 상어 배열이 작을 수도 있으니까
            shark[r][c] = group_ball[t]
            t += 1
        else:                                       # 작다면 나머지는 0으로 채운다.
            shark[r][c] = 0


def cnt_break():            # 연속한 4개의 구슬을 터뜨리는 함수
    global flag
    y, x = snail[-1]
    number = shark[y][x]
    cnt = 1
    bomb = [[y, x]]
    for i_idx in range(len(snail)-2, -1, -1):
        y_idx, x_idx = snail[i_idx]
        if shark[y_idx][x_idx] == number:
            cnt += 1
            bomb.append([y_idx, x_idx])         # 일단 4개가 될지 모르니 좌표를 넣어준다.

        else:
            if cnt >= 4:                        # 개수가 4개가 넘는다면
                while bomb:
                    flag = True                 # 터뜨렸다는것을 확인해주고
                    y, x = bomb.pop()           # 해당 좌표를 0으로 바꿔주고
                    shark[y][x] = 0             # 구슬을 더해준다.
                    stone[number] += 1
            cnt = 1                             # 개수와 터뜨리는 좌표의 리스트를 초기화 해줌
            bomb.clear()
            bomb = [[y_idx, x_idx]]
        number = shark[y_idx][x_idx]


def move_ball():                  # 빈 공간 채우는 함수
    stack = []
    for idx in range(len(snail)):
        yy, xx = snail[idx]
        if shark[yy][xx]:
            stack.append(shark[yy][xx])

    for idx in range(len(snail)-1, -1, -1):
        yy, xx = snail[idx]
        if stack:
            shark[yy][xx] = stack.pop()
        else:
            shark[yy][xx] = 0


def broken(b_size, num):            # 블리자드 마법 시전
    for idx in range(num+1, len(snail)):
        r, c = snail[idx]
        if b_size == shark[r][c]:
            shark[r][c] = 0
        else:
            break

    for idx in range(num-1, -1, -1):
        r, c = snail[idx]
        if b_size == shark[r][c]:
            shark[r][c] = 0
        else:
            break


N, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(N)]
rock = [list(map(int, input().split())) for _ in range(M)]

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
d = [4, 2, 3, 1]
snail = [(0, 0)]

visit = [[0]*N for _ in range(N)]
visit[0][0] = 1

i, j, direc = 0, 0, 0
stone = {1: 0, 2: 0, 3: 0}

# 달팽이 구현
while True:
    if i == N//2 and j == N//2:
        break

    ni = i + dy[d[direc]]
    nj = j + dx[d[direc]]

    if ni < 0 or nj < 0 or ni >= N or nj >= N or visit[ni][nj]:
        direc = (direc + 1) % 4
        continue
    else:
        snail.append((ni, nj))
        visit[ni][nj] = 1

    i, j = ni, nj

ay, by = snail.pop()

for i in rock:
    a, b = ay, by
    for j in range(i[1]):
        a += dy[i[0]]
        b += dx[i[0]]
        for k in range(len(snail)):
            if snail[k] == (a, b):
                shark[a][b] = 0
                broken(shark[a][b], k)
                break

    while True:         # 빈칸 채우기, 구슬 깨기 무한 반복
        move_ball()
        flag = False
        cnt_break()
        if not flag:
            break

    change_ball()
ans = stone[1] + 2*stone[2] + 3*stone[3]
print(ans)









