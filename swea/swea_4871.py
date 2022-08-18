T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        N, M = map(int, input().split())
        arr[N][M] = 1                                     # 일방 통행

    start, end = map(int, input().split())

    stack = [start]
    visited = [start]
    ans = 0
    while stack:
        i = stack.pop()

        if i not in visited:
            visited.append(i)
        if i == end:
            ans = 1
            break

        for idx in range(1, V+1):
            if not arr[i][idx] or idx in visited:
                continue

            else:
                stack.append(idx)

    print(f"#{tc} {ans}")