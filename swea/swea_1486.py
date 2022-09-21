# 조합으로 풀려고 했지만... 시간초과
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    li = list(map(int, input().split()))
    ans = 987654321
    for i in range(1 << N):
        sum_set = []
        visited = [0] * N
        for j in range(N):
            if i & (1 << j):
                sum_set.append(li[j])
        if sum(sum_set) >= K:
            if ans > sum(sum_set):
                ans = sum(sum_set)
    print(f"#{tc} {ans - K}")