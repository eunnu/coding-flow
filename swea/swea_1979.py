T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        cnt_x, cnt_y = 0, 0
        for j in range(N):
            if arr[i][j]:
                cnt_x += 1
                if j == N-1 and cnt_x == K:
                    ans += 1
            elif not arr[i][j]:
                if cnt_x == K:
                    ans += 1
                cnt_x = 0

            if arr[j][i]:
                cnt_y += 1
                if j == N-1 and cnt_y == K:
                    ans += 1
            elif not arr[j][i]:
                if cnt_y == K:
                    ans += 1
                cnt_y = 0

    print(f"#{tc} {ans}")