# 완전 탐색으로 풀어볼 예정
from collections import deque
from heapq import heappush


def choice():
    global fuel, dis, ans
    tmp = taxi+[0]
    queue = deque()
    queue.append(tmp)

    visit = set()

    while queue:
        y, x, cnt = queue.popleft()

        visit.add((y, x))

        if cnt > fuel:
            ans = -1
            fuel = -1
            break

        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]

            if 1 <= ny <= N and 1 <= nx <= N:
                if (ny, nx) not in visit:
                    if not load_map[ny][nx]:
                        if (ny, nx) in people_s and [cnt + 1, ny, nx, people_s[(ny, nx)]] not in dis:
                            heappush(dis, [cnt + 1, ny, nx, people_s[(ny, nx)]])
                            visit.add((y, x))
                        queue.append([ny, nx, cnt + 1])


def move(start):
    global fuel, taxi, ans, people_d

    fuel -= start[0]
    moving = deque()
    moving.append([start[1], start[2], 0])

    visit = set()

    flag = False
    while moving:
        y, x, cnt = moving.popleft()
        if cnt > fuel:
            break

        if (y, x) in people_d.keys() and start[3] in people_d[(y, x)]:
            fuel += cnt
            taxi = [y, x]
            flag = True
            break

        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]

            if 1 <= ny <= N and 1 <= nx <= N:
                if load_map[ny][nx] == 0 and (ny, nx) not in visit:
                    visit.add((ny, nx))
                    moving.append((ny, nx, cnt+1))

    if not flag:
        fuel = -1
        ans = -1


N, M, fuel = map(int, input().split())
load_map = [[0] * (N+1)]
load_map += [[0] + list(map(int, input().split())) for _ in range(N)]
taxi = list(map(int, input().split()))

people_s = dict()
people_d = dict()
for i in range(M):
    a, b, c, d = map(int, input().split())
    people_s[(a, b)] = i
    if (c, d) not in people_d:
        people_d[(c, d)] = []
    people_d[(c, d)].append(i)

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

ans = 0
for _ in range(M):
    if fuel < 0:
        break
    dis = []
    if (taxi[0], taxi[1]) in people_s.keys():
        dis.append([0, taxi[0], taxi[1], people_s[(taxi[0], taxi[1])]])
    else:
        choice()
    if fuel < 0 or (not dis):
        fuel = -1
        break
    move(dis[0])
    people_s.pop((dis[0][1], dis[0][2]))

if ans >= 0:
    ans = fuel

print(ans)