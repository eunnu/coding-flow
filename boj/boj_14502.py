def bfs():
    global safe, ans
    mz = safe - 3
    lab_cpy2 = []
    for i_idx in range(N):
        temp = []
        for j_jdx in range(M):
            temp.append(lab_cpy[i_idx][j_jdx])
        lab_cpy2.append(temp)

    queue = []
    for i_idx in range(len(origin)):
        temp = origin[i_idx]
        queue.append(temp)

    while queue:
        y, x = queue.pop(0)

        for dire in range(4):
            ny = y + dy[dire]
            nx = x + dy[dire]

            if 0 <= ny < N and 0 <= nx < N and not lab_cpy2[ny][nx]:
                lab_cpy2[ny][nx] = 2
                mz -= 1
                queue.append((ny, nx))

    ans = max(mz, ans)


def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for idx in range(N):
        for jdx in range(M):
            if not lab_cpy[i][j]:
                lab_cpy[i][j] = 1
                wall(cnt+1)
                lab_cpy[i][j] = 0



N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

origin = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

safe = 0
for i in range(N):
    for j in range(M):
        if not lab:
            safe += 1
        elif lab[i][j] == 2:
            origin.append((i, j))

ans = 0
for i in range(N):
    for j in range(M):
        lab_cpy = []
        if not lab[i][j]:
            for k in range(N):
                tmp = []
                for z in range(M):
                    tmp.append(lab[k][z])
                lab_cpy.append(tmp)

            lab_cpy[i][j] = 1
            wall(1)
            lab_cpy[i][j] = 0

print(ans)