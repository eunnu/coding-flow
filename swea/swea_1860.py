T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    host = list(map(int, input().split()))
    host.sort()
    ans = 'Possible'
    t = 1
    for i in range(0, N, K):
        if host[i] < M * t:
            ans = 'Impossible'
            break
        if i >= N:
            break
        t += 1

    print(f"#{tc} {ans}")
