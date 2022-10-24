# 달팽이 모양으로 리스트에 좌표를 순서대로 넣어준다.
# 방향으로 돌이 던져 지면 해당 좌표에서 좌우, 상하로 퍼지면서 이웃하는 돌의 크기를 확인해준다.
# 달팽이 모양 좌표 리스트를 역으로 돌면서 값이 존재하면 그 값들을 넣어준다.
# 기존 배열에서 달팽이 리스트를 역으로 다시 값 들을 초기화 시켜준다.
def broken(b_size, num):
    for idx in range(num+1, len(snail)):
        r, c = snail[idx]
        if b_size == shark[r][c]:
            stone[b_size] += 1
            shark[r][c] = 0
        else:
            break

    for idx in range(num-1, -1, -1):
        r, c = snail[idx]
        if b_size == shark[r][c]:
            stone[b_size] += 1
            shark[r][c] = 0
        else:
            break


N, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(N)]
rock = [list(map(int, input().split())) for _ in range(M)]

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
d = [4, 2, 3, 1]
snail = [(0, 0)]

visit = [[0]*N for _ in range(N)]
visit[0][0] = 1

i, j, direc = 0, 0, 0
stone = {1: 0, 2: 0, 3: 0}

# 달팽이 구현
while True:
    if i == N//2 and j == N//2:
        break

    ni = i + dy[d[direc]]
    nj = j + dx[d[direc]]

    if ni < 0 or nj < 0 or ni >= N or nj >= N or visit[ni][nj]:
        direc = (direc + 1) % 4
        continue
    else:
        snail.append((ni, nj))
        visit[ni][nj] = 1

    i, j = ni, nj

ay, by = snail.pop()

for i in rock:
    a, b = ay, by
    for j in range(i[1]):
        a += dy[i[0]]
        b += dx[i[0]]
        for k in range(len(snail)):
            if snail[k] == (a, b):
                stone[shark[a][b]] += 1
                shark[a][b] = 0
                broken(shark[a][b], k)
                break





