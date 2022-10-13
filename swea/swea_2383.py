# 일단 계단까지 걸리는 시간을 구해서 오름차순으로 정렬해놓는다.
# 앞에 3사람 먼저 계단 내려가고 하나씩 채워 넣는 식으로

for tc in range(1, int(input())+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    person = []
    stairs = []
    k = 1
    for i in range(N):
        for j in range(N):
            if li[i][j] == 1:
                person.append([k, i, j])
                k += 1
            elif li[i][j] > 1:
                stairs.append([li[i][j], i, j])
    stairs.sort()
    dist = []
    for i in range(2):
        tmp = []
        st = stairs[i]
        for j in person:
            d = abs(j[1] - st[1]) + abs(j[2] - st[2])
            tmp.append([j[0], d+1, 0])

        tmp.sort(key=lambda x: x[1])
        dist.append(tmp)

    visit = [1] + [0]*len(person)
    complete = [1] + [0]*len(person)
    ans = 1
    maxi_1 = 0
    maxi_2 = 0

    while True:
        ans += 1
        for i in range(len(person)):
            if visit[dist[0][i][0]] and not complete[dist[0][i][0]] and stairs[0][0] == dist[0][i][2]:
                maxi_1 -= 1
                complete[dist[0][i][0]] = 1
            if visit[dist[1][i][0]] and not complete[dist[1][i][0]] and stairs[1][0] == dist[1][i][2]:
                maxi_2 -= 1
                complete[dist[1][i][0]] = 1

            if maxi_1 < 3:
                if not visit[dist[0][i][0]] and ans >= dist[0][i][1]:
                    visit[dist[0][i][0]] = 1
                    dist[0][i][2] += 1
                    maxi_1 += 1
            if maxi_2 < 3:
                if not visit[dist[1][i][0]] and ans >= dist[1][i][1]:
                    visit[dist[1][i][0]] = 1
                    dist[1][i][2] += 1
                    maxi_2 += 1

            if visit[dist[0][i][0]] and stairs[0][0] > dist[0][i][2]:
                dist[0][i][2] += 1
            if visit[dist[1][i][0]] and stairs[1][0] > dist[1][i][2]:
                dist[1][i][2] += 1

        if 0 not in complete:
            break

    print(f"#{tc} {ans}")