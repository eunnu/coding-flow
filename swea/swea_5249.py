def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(E)]

    li.sort(key=lambda x: x[2])

    p = [i for i in range(V+1)]

    ans = cnt = 0
    for i in li:
        num1, num2, w = i
        if find_set(num1) != find_set(num2):
            union(num1, num2)
            ans += w
            cnt += 1
        if cnt == V:
            break

    print(f"#{tc} {ans}")