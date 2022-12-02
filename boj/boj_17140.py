from collections import deque


def sorting(b):   # 주어진 정렬 조건대로 정렬
    reb = deque()
    while sum(b) > 0:
        d = max(b)
        if sum(b) == 0:
            break
        for ldx in range(len(b)-1, -1, -1):  # 두가지 정렬 조건을 만족시키기 위해 뒤에서 부터 반복
            if b[ldx] == d:
                b[ldx] = 0
                reb.appendleft(d)       # 수가 먼저 와야 하기 때문에 개수를 먼저 넣어줌
                reb.appendleft(ldx)
                break
    return reb


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

y = x = 3
ans = t = 0
while True:
    if y >= r and x >= c and A[r-1][c-1] == k:
        ans = t
        break

    if t > 100:
        ans = -1
        break

    mx, my = x, y
    if y >= x:
        A_li = [[0]*(2*y) for _ in range(y)]        # 최대 길이는 현재 길이 * 2
        for i in range(y):
            tmp = [0] * 101                         # 숫자가 최대 100까지 이므로 개수를 넣어줄 배열
            for j in range(x):
                if A[i][j]:
                    tmp[A[i][j]] += 1
            sol = sorting(tmp)
            mx = max(mx, len(sol))                  # 행 열 길이를 비교하기 위한 업데이트
            for s in range(len(sol)):
                A_li[i][s] = sol[s]

    else:
        A_li = [[0]*x for _ in range(2*x)]
        for i in range(x):
            tmp = [0] * 101
            for j in range(y):
                if A[j][i]:
                    tmp[A[j][i]] += 1
            sol = sorting(tmp)
            my = max(my, len(sol))
            for s in range(len(sol)):
                A_li[s][i] = sol[s]

    A.clear()
    x, y = mx, my
    A = [[0]*x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            A[i][j] = A_li[i][j]

    t += 1

print(ans)
