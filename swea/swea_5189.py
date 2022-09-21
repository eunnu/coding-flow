# 뒤의 인덱스를 타고 들어가야 함
def perm(depth, destination, cnt):
    global ans
    if cnt > ans:
        return
    if depth == N:
        if cnt < ans:
            ans = cnt
        return

    else:
        for idx in range(N):
            if depth < N - 1 and idx != 0:
                if not visited[idx] and destination != idx:
                    visited[idx] = 1
                    perm(depth + 1, idx, cnt+li[destination][idx])
                    visited[idx] = 0
            elif depth == N-1:
                perm(depth+1, 0, cnt+li[destination][0])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    ans = 987654321
    perm(0, 0, 0)
    print(f"#{tc} {ans}")
