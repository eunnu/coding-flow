T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N = N//10

    dp = [0, 1, 3]
    for i in range(3, N+1):
        dp.append(dp[i-1]+dp[i-2]*2)

    print(f"#{tc} {dp[-1]}")