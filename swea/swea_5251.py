def prim():
    dist = [987654321] * (V+1)
    dist[0] = 0
    visited = [0]*(V+1)

    for _ in range(V+1):

        mini = 987654321
        index = -1

        for idx in range(V+1):
            if not visited[idx] and mini > dist[idx]:
                index = idx
                mini = dist[idx]

        visited[index] = 1

        for idx in range(V+1):
            if not visited[idx] and arr[index][idx] + dist[index] < dist[idx]:
                dist[idx] = arr[index][idx] + dist[index]

    return dist[V]


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    arr = [[987654321]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        st, ed, w = map(int, input().split())
        arr[st][ed] = w

    print(f"#{tc}", prim())