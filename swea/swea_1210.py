import sys
sys.stdin = open("input.txt", "r")

T = 10                                                                 # 테스트 케이스 수 : 10

dx = [-1, 1, 0]
dy = [0, 0, -1]

for _ in range(T):                                                      # 1부터 T까지 반복
    tc = int(input())                                                   # tc 번호 입력 받음

    ladder = []

    for i in range(100):
        ladder.append(list(map(int, input().split())))

    ans = 0
    x, y = 0, 99
    for i in range(100):
        if ladder[99][i] == 2:
            x = i

    direc = 0
    while True:
        nx = x + dx[direc]
        ny = y + dy[direc]

        if ny == 0 and ladder[ny][nx]:
            ans = nx
            break

        if nx < 0 or ny < 0 or nx > 99 or ny > 99 or ladder[ny][nx] == 0:
            direc += 1
            continue

        cnt = 0
        temp_x = nx
        temp_y = ny
        flag = False
        direc_c = direc
        while True:

            direc_c += 1
            if direc_c > 2:
                direc_c = 0

            cx = temp_x + dx[direc_c]
            cy = temp_y + dy[direc_c]

            if cy == 0 and ladder[cy][cx]:
                flag = True
                ans = cx
                break

            if temp_x < 0 or temp_y < 0 or temp_x > 99 or temp_y > 99 or ladder[temp_y][temp_x] == 0:
                direc += 1
                continue

            temp_x = cx
            temp_y = cy

            cnt += 1

            if cnt > 3:
                break

            if flag:
                break

        x = nx
        y = ny
        direc_c += 1

        if direc > 2:
            direc = 0

    print(f"#{tc} {ans}")
