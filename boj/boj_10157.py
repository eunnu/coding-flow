'''
상우하좌 순으로 진행 더이상 진행 할 수 없으면 방향을 바꾸어줌
가로 세로 입력받음 -> 세로 가로로 풀이
'''

x_len, y_len = map(int, input().split())
seat = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

y, x = 1, 1
arr = [[0]*(y_len+1) for _ in range(x_len+1)]
num = 1
arr[y][x] = 1
if x_len*y_len < seat:
    print(0)
else:
    d = 0
    flag = True
    while flag:
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 1 or nx < 1 or ny > x_len or nx > y_len or arr[ny][nx]:
            d += 1
            if d == 4:
                d = 0
            continue

        num += 1
        if num == seat:
            print(ny, nx)
            flag = False

        arr[ny][nx] = num
        y = ny
        x = nx

    print(arr)