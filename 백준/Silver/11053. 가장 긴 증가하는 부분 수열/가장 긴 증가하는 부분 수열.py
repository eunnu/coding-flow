from sys import stdin

N = int(stdin.readline())
array = [0] + list(map(int, stdin.readline().split(" ")))
res = 0
dp = [1]*(N+1)

for i in range(N, 0, -1):
    max_cnt = dp[i]
    for j in range(i, N+1):
        if array[i] < array[j]:
            if max_cnt < dp[j] + 1:
                max_cnt = dp[j] + 1

    dp[i] = max_cnt

print(max(dp))

