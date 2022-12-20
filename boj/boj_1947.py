N = int(input())
dp = [0, 0, 1]
if N > 2:
    for i in range(3, N+1):
        dp.append((dp[i-1] + dp[i-2]) * (i-1) % 1000000000)
        # 점화식을 찾아내 버림
print(dp[N])