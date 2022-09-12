'''
연결되어 있는 양의 수 <= 늑대의 수 : 늑대의 수를 ++
연결되엉 있는 양의 수 > 늑대의 수 : 양의 수를 ++
세로, 가로 입력 순 
# : 지나갈 수 없음
. : 지나갈 수 있음
V : 늑대
O : 양
'''

y, x = map(int, input().split())
area = []

num_s, num_w = 0, 0
for i in range(y):
    area.append(list(input()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = set()
stack = []

for r in range(y):
    for c in range(x):
        if (r, c) in visited or area[r][c] == '#':
            continue
        o, v = 0, 0
        if area[r][c] == 'o':
            o += 1
        if area[r][c] == 'v':
            v += 1
        stack.append([r, c])
        while stack:
            [sy, sx] = stack.pop()
            visited.add((sy, sx))

            for i in range(4):
                ny = sy + dy[i]
                nx = sx + dx[i]

                if ny < 0 or nx < 0 or ny >= y or nx >= x or (ny, nx) in visited:
                    continue

                if area[ny][nx] == '#':
                    continue

                if area[ny][nx] == 'o':
                    o += 1

                if area[ny][nx] == 'v':
                    v += 1

                stack.append([ny, nx])

        if o <= v:
            num_w += v
            v, o = 0, 0
        else:
            num_s += o
            v, o = 0, 0

print(num_s, num_w)


