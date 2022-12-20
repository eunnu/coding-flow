N = int(input())

ans = 0
if N % 2:
    ans = 0

dp = [1, 0, 1, 0, 2]
if N > 4:
    for i in range(5, N+1):
        if i % 2:
            dp.append(0)
        else:
            dp.append((dp[i-2] * dp[i-4] + i//2) % 987654321)

print(dp[N])