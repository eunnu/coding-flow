from sys import stdin

N = int(stdin.readline())
pm = [list(map(int, stdin.readline().split(" "))) for _ in range(N)]

dp = [[0]*i for i in range(1, N+1)]
dp[0][0] = pm[0][0]
for i in range(1, N):
    for j in range(i+1):
        if 0 < j < i:
            dp[i][j] = max(dp[i-1][j] + pm[i][j], dp[i-1][j-1] + pm[i][j])
        elif j == 0:
            dp[i][j] = dp[i-1][j] + pm[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + pm[i][j]

print(max(dp[-1]))