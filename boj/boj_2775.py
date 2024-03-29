T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apart = [[i for i in range(1, 15)]] + [[0] * 15 for _ in range(k)]
    for i in range(1, k + 1):
        apart[i][0] = 1
        for j in range(1, n):
            apart[i][j] = apart[i][j - 1] + apart[i - 1][j]
    print(apart[k][n-1])


