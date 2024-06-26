from sys import stdin

inp = stdin.readline
N = int(inp())
pipe = [list(map(int, inp().split(" "))) for _ in range(N)]

dp = [[[] for _ in range(N)] for _ in range(N)]
for i in range(1, N):
    if not pipe[0][i]:
        dp[0][i].append(3)
    elif pipe[0][i]:
        break

for i in range(1, N):
    for j in range(1, N):
        if not pipe[i][j]:
            if dp[i-1][j] != [] and (4 in dp[i-1][j] or 5 in dp[i-1][j]):
                for k in dp[i-1][j]:
                    if k == 4 or k == 5:
                        dp[i][j].append(4)
            if dp[i][j-1] != [] and (3 in dp[i][j-1] or 5 in dp[i][j-1]):
                for k in dp[i][j-1]:
                    if k == 3 or k == 5:
                        dp[i][j].append(3)
            if dp[i-1][j-1]:
                if pipe[i-1][j] or pipe[i][j-1]:
                    continue

                for k in dp[i-1][j-1]:
                    if k == 4 or k == 5 or k == 3:
                        dp[i][j].append(5)



print(len(dp[N-1][N-1]))