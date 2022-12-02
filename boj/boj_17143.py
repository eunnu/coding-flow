# 한 칸에 한마리만 들어갈 수 있는데 다른 상어가 있으면 큰 상어가 잡아먹음
# 이때, 잡아먹은 상어의 크기나 방향에는 영향을 미치지 않음
# 낚시꾼이 서있는 열에서 가장 가까운 상어를 잡음
def move():
    after = dict()
    for ss in shark.keys():
        num = shark[ss]
        di = sh[num][1]
        sd = sh[num][0]

        ny, nx = ss
        if di == 1 or di == 2:
            tmp = (R - 1) * 2                   # 왕복 길이
            if tmp <= sd:                       # 만약 그 길이보다 속도가 크면 나머지 만큼만 계산하겠단 뜻
                sd = sd % tmp

            for idx in range(sd):
                ny += dy[di]                    # 0보다 작은 경우는 위로 올라간 경우이므로 1보다 작으면 1로 가야 하니 2를 더하고
                if ny < 1:
                    ny += 2
                    di = sh[num][1] = 2
                elif ny > R:                    # R 보다 큰 경우는 아래로 내려간 경우이므로 2를 빼주고 방향은 위로 전환
                    ny -= 2
                    di = sh[num][1] = 1

        else:
            tmp = (C - 1) * 2
            if tmp <= sd:
                sd = sd % tmp
            for idx in range(sd):
                nx += dx[di]

                if nx < 1:
                    nx += 2
                    di = sh[num][1] = 3
                elif nx > C:
                    nx -= 2
                    di = sh[num][1] = 4

        if (ny, nx) not in after:                           # 이동 후 상어가 안겹치면 그냥 넣어주고
            after[(ny, nx)] = num
        else:                                               # 아니면 덩치 큰 상어를 넣어줌
            if sh[after[(ny, nx)]][2] < sh[num][2]:
                after[(ny, nx)] = num

    return after


R, C, M = map(int, input().split())
shark = dict()
sh = []
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[(r, c)] = i
    sh.append([s, d, z])

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]
get = [0]*M
king = 0
ans = 0
for j in range(1, C+1):
    for i in range(1, R+1):
        if (i, j) in shark:
            ans += sh[shark[(i, j)]][2]
            shark.pop((i, j))
            break
    shark = move()

print(ans)