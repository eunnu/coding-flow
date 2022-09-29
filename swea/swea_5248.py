def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))

    p = [i for i in range(N+1)]
    for i in range(0, M):
        if find_set(li[2*i]) != find_set(li[2*i + 1]):
            union(li[2*i], li[2*i + 1])

    for i in range(1, len(p)):
        find_set(i)

    p = list(set(p))
    print(f"#{tc} {len(p)-1}")
