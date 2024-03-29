tc = int(input())

for _ in range(tc):
    n = int(input())

    arr = [0] + list(map(int, input().split(" ")))
    sum_arr = [0]

    for i in range(1, n+1):
        sum_arr.append(sum_arr[i-1]+arr[i])

    dp = [[0]*(n+2) for _ in range(n+2)]
    for i in range(2, n+1):
        for j in range(i-1, 0, -1):
            dp[j][i] = 987654321
            for k in range(j, i+1):
                dp[j][i] = min(dp[j][i], dp[j][k] + dp[k + 1][i])

            dp[j][i] += sum_arr[i] - sum_arr[j - 1]

    print(dp[1][n])