# 오른쪽이랑 아래로만 움직일 수 있기 때문에
# DP로 풀생각

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]
    dp[0][0] = li[0][0]
    for i in range(N):
        for j in range(N):
            if j == 0:
                dp[i][j] = li[i][j] + dp[i-1][j]
            elif i == 0:
                dp[i][j] = li[i][j] + dp[i][j-1]
            else:
                dp[i][j] = li[i][j] + min(dp[i-1][j], dp[i][j-1])

    print(f"#{tc} {dp[N-1][N-1]}")