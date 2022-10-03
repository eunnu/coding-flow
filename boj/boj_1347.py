N = int(input())
maze = input()

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
direction = [[1, 3], [2, 0], [3, 1], [0, 2]]

y = x = d = 0
jun = [[0, 0]]

min_x = min_y = 0
for i in maze:
    if i == "R":
        d = direction[d][0]
    elif i == "L":
        d = direction[d][1]
    else:
        y += dy[d]
        x += dx[d]
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    if [y, x] not in jun:
        jun.append([y, x])

max_y = max_x = 0
for i in range(len(jun)):
    jun[i][0] += min_y*(-1)
    jun[i][1] += min_x*(-1)
    max_y = max(max_y, jun[i][0])
    max_x = max(max_x, jun[i][1])

ans = [['#']*(max_x + 1) for _ in range(max_y + 1)]

for i in jun:
    ans[i[0]][i[1]] = '.'

for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end="")
    print()