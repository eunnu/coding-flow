from sys import stdin

N, M = map(int, stdin.readline().split(" "))
num = [list(map(int, stdin.readline().split(" "))) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not i and not j:
            continue

        if i and j:
            num[i][j] += num[i-1][j] + num[i][j-1] - num[i-1][j-1]
        elif not i:
            num[i][j] += num[i][j-1]
        elif not j:
            num[i][j] += num[i-1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split(" "))
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if not x1 and not y1:
        print(num[x2][y2])
    elif not x1:
        print(num[x2][y2] - num[x2][y1-1])
    elif not y1:
        print(num[x2][y2] - num[x1-1][y2])
    else:
        print(num[x2][y2] - num[x1-1][y2] - num[x2][y1-1] + num[x1-1][y1-1])


