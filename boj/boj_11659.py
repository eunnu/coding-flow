from sys import stdin

N, M = map(int, stdin.readline().split(" "))
arr = list(map(int, stdin.readline().split(" ")))
res = [0] * (N + 1)
res[1] = arr[0]
for i in range(2, N + 1):
    res[i] = res[i - 1] + arr[i - 1]
for _ in range(M):
    fir, sec = map(int, stdin.readline().split(" "))
    print(res[sec] - res[fir - 1])