'''
연결되어 있는 양의 수 <= 늑대의 수 : 늑대의 수를 ++
연결되엉 있는 양의 수 > 늑대의 수 : 양의 수를 ++
세로, 가로 입력 순
# : 지나갈 수 없음
. : 지나갈 수 있음
V : 늑대
O : 양
'''

Y, X = map(int, input().split())
area = [list(input()) for _ in range(Y)]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

sheep, wolf = 0, 0

for i in range(Y):
    for j in range(X):
        stack = [[i, j]]
        cnt_s, cnt_w = 0, 0

        if area[i][j] == '#':
            continue

        while stack:
            y, x = stack.pop()

            if area[y][x] == 'v':
                cnt_w += 1

            elif area[y][x] == 'o':
                cnt_s += 1

            area[y][x] = '#'

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < X and 0 <= ny < Y:
                    if area[ny][nx] != '#':
                        stack.append([ny, nx])

        if cnt_s > cnt_w:
            sheep += cnt_s
        else:
            wolf += cnt_w

print(sheep, wolf)