N, M, D = map(int, input().split())

area = []
for i in range(N):
    area.append(list(map(int, input().split())))

sh = []
for i in range(M):
    cnt = 0
    for j in range(N):
        cnt += area[j][i]
    sh.append([cnt, i])

sh.sort()
dy = [-1, 0, 0]
dx = [0, -1, 1]



