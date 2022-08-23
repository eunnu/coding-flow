def perm(idx, ans):
    global res
    if ans > res:
        return

    if idx == N:
        if res > ans:
            res = ans
        return

    else:
        for i in range(N):
            if not visit[i]:
                visit[i] = 1
                perm(idx+1, ans + arr[idx][i])
                visit[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    visit = [0]*N
    res = 987654321

    perm(0, 0)

    print(f"#{tc} {res}")