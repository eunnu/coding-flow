def perm(idx, sum_idx):
    global ans
    if sum_idx > ans:
        return

    if idx == N:
        if sum_idx < ans:
            ans = sum_idx
        return

    else:
        for i in range(N):
            if not visit[i]:
                visit[i] = 1
                perm(idx + 1, sum_idx + arr[idx][i])
                visit[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    visit = [0] * N
    ans = 987654321
    perm(0, 0)

    print(f"#{tc} {ans}")