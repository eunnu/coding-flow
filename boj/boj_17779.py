# x, y, d1, d2의 를 계속 바꿔주면서 완탐
# 해당 되는 범위들을 인덱스로 계산하여 범위를 지정

def sol(x, y, d1, d2):
    global ans
    five = set()

    for idx in range(d1+1):
        five.add((x+idx, y-idx))
        five.add((x+d2+idx, y+d2-idx))
        for jdx in range(y-idx, y+1):
            five.add((x+idx, jdx))
        for jdx in range(y+d2-d1, y+d2-idx+1):
            five.add((x+d2+idx, jdx))
    for idx in range(d2+1):
        five.add((x+idx, y+idx))
        five.add((x+d1+idx, y-d1+idx))
        for jdx in range(y, y+idx+1):
            five.add((x+idx, jdx))
        for jdx in range(y-d1+idx, y+d2-d1+1):
            five.add((x+d1+idx, jdx))
    people = [0]*5

    # 1번 선거구
    for idx in range(1, x+d1):
        for jdx in range(1, y+1):
            if 1 <= idx <= N and 1 <= jdx <= N:
                if (idx, jdx) not in five:
                    people[0] += li[idx][jdx]

    # 2번 선거구
    for idx in range(1, x+d2+1):
        for jdx in range(y+1, N+1):
            if 1 <= idx <= N and 1 <= jdx <= N:
                if (idx, jdx) not in five:
                    people[1] += li[idx][jdx]

    # 3번 선거구
    for idx in range(x+d1, N+1):
        for jdx in range(1, y-d1+d2):
            if 1 <= idx <= N and 1 <= jdx <= N:
                if (idx, jdx) not in five:
                    people[2] += li[idx][jdx]

    # 4번 선거구
    for idx in range(x+d2+1, N+1):
        for jdx in range(y-d1+d2, N+1):
            if 1 <= idx <= N and 1 <= jdx <= N:
                if (idx, jdx) not in five:
                    people[3] += li[idx][jdx]

    for idx in five:
        if 1 <= idx[0] <= N and 1 <= idx[1] <= N:
            people[4] += li[idx[0]][idx[1]]

    tmp = max(people) - min(people)
    ans = min(ans, tmp)


N = int(input())
li = [[0] * (N + 1)]
for _ in range(N):
    li.append([0]+list(map(int, input().split())))

ans = 987654321
for i in range(1, N+1):
    for j in range(2, N+1):
        for k in range(1, j):
            for l in range(1, N-j+1):
                sol(i, j, k, l)

print(ans)