# 이동경로에 따라 가능한 충전소들의 충전소의 정보를 넣어준다.
# 같은 경로가 존재 할 경우 인원으로 나눈 값이 큰지 아니면 따로의 합이 더 큰지 확인 후 더해준다.
# A 유저는 1, 1 출발, B 유저는 10, 10 출발

for tc in range(1, int(input())+1):
    M, A = map(int, input().split())

    a_user = list(map(int, input().split()))
    b_user = list(map(int, input().split()))

    a_load = []
    b_load = []

    dy = [0, -1, 0, 1, 0]
    dx = [0, 0, 1, 0, -1]

    cs = [list(map(int, input().split())) for _ in range(A)]

    a_li = [0] * A
    b_li = [0] * A
    for i in range(A):

        if abs(cs[i][0] - 1) + abs(cs[i][1] - 1) <= cs[i][2]:
            a_li[i] = 1
        if abs(cs[i][0] - 10) + abs(cs[i][1] - 10) <= cs[i][2]:
            b_li[i] = 1

    a_load.append(a_li)
    b_load.append(b_li)

    a_x = a_y = 1
    b_x = b_y = 10

    for i in range(M):
        a_x += dx[a_user[i]]
        a_y += dy[a_user[i]]
        b_x += dx[b_user[i]]
        b_y += dy[b_user[i]]

        a_li = [0]*A
        b_li = [0]*A

        for j in range(A):
            if abs(cs[j][1] - a_y) + abs(cs[j][0] - a_x) <= cs[j][2]:
                a_li[j] = 1
            if abs(cs[j][1] - b_y) + abs(cs[j][0] - b_x) <= cs[j][2]:
                b_li[j] = 1

        a_load.append(a_li)
        b_load.append(b_li)

    ans = 0
    for i in range(M+1):
        a_tmp = b_tmp = 0
        flag = False
        num = -1
        for j in range(A):
            if a_load[i][j] and a_load[i][j] == b_load[i][j]:
                flag = True
                if num:
                    if cs[num][3] < cs[j][3]:
                        num = j
                else:
                    num = j

            elif a_load[i][j]:
                if a_tmp < cs[j][3]:
                    a_tmp = cs[j][3]

            elif b_load[i][j]:
                if b_tmp < cs[j][3]:
                    b_tmp = cs[j][3]
        if flag:
            ans += max(a_tmp + b_tmp, a_tmp + cs[num][3], b_tmp + cs[num][3], cs[num][3])
        else:
            ans += a_tmp + b_tmp

    print(f"#{tc} {ans}")