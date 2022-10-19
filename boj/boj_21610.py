# 처음에는 (N, 1), (N, 2), (N-1, 1), (N-1, 2)
# 방향은 8방향 1 ~ 8
# 인덱스는 1 ~ N 까지
# 물의 양이 2 이상이어야 구름이 생기고 2만큼 줄어든다. 구름이 사라진 칸은 제외
from pprint import pprint


def make_cloud():           # 새로운 구름 리스트 생성 중
    for idx in range(1, N+1):
        for jdx in range(1, N+1):
            if b[idx][jdx] >= 2 and (idx, jdx) not in no_cloud:     # 현재 인덱스의 물이 2 이상이고 구름이 사라진 위치가 아니라면
                cloud.append([idx, jdx])
                b[idx][jdx] -= 2            # 구름리스트에 넣어주고 -2 해준다.


def plus_water():           # 물 넣어주는 중
    for cl in cloud:
        cnt = 0
        no_cloud.add((cl[0], cl[1]))    # 구름 사라진 위치 넣어주는 중
        for p in pls:                   # 대각선 확인하는 중
            ny = cl[0] + dy[p]
            nx = cl[1] + dx[p]
            if 0 < ny <= N and 0 < nx <= N:
                if b[ny][nx] > 0:
                    cnt += 1

        b[cl[0]][cl[1]] += cnt          # 물이 있는 곳 만큼 넣어주는 중


def moving(d, num):                     # 구름이 움직이는 중
    for c in range(len(cloud)):
        y = cloud[c][0]
        x = cloud[c][1]
        for _ in range(num):
            y += dy[d]
            x += dx[d]
            if y > N:
                y = 1
            elif y < 1:
                y = N
            if x > N:
                x = 1
            elif x < 1:
                x = N
        cloud[c][0], cloud[c][1] = y, x

    for c in cloud:
        b[c[0]][c[1]] += 1


N, M = map(int, input().split())
b = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[N, 1], [N, 2], [N-1, 1], [N-1, 2]]
pls = [2, 4, 6, 8]

for m in move:
    moving(m[0], m[1])
    no_cloud = set()
    plus_water()
    cloud = []
    make_cloud()

ans = 0
for i in range(1, N+1):
    ans += sum(b[i])

print(ans)