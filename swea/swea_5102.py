'''
주어진 경로를 움직일 때 마다 + 1 한 값을 queue 에 같이 넣어줌
인접 행렬로 풀 예정
'''


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
        arr[end][start] = 1

    S, G = map(int, input().split())

    queue = [[S, 0]]
    visit = []

    ans = 0
    while queue:
        [idx, cnt] = queue.pop(0)
        if idx == G:
            ans = cnt
            break

        if idx not in visit:
            visit.append(idx)

        for i in range(V+1):
            if arr[idx][i] and i not in visit:
                queue.append([i, cnt + 1])

    print(f"#{tc} {ans}")