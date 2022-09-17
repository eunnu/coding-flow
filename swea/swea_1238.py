# 일단 입력 받은 걸로 배열로 변환


for tc in range(1, 11):
    N, start = map(int, input().split())
    li = list(map(int, input().split()))
    M = max(li)
    tree = [[0]*(M+1) for _ in range(M+1)]
    for i in range(N//2):
        tree[li[2*i]][li[2*i+1]] = 1
    ans = start
    stack = [[start]]
    visited = set()
    visited.add(start)
    while stack != [[]]:
        idx = stack.pop()
        tmp = []
        for j in idx:
            for i in range(M+1):
                if tree[j][i] and i not in visited:
                    tmp.append(i)
                    visited.add(i)
        stack.append(tmp)

    print(f"#{tc} {ans}")

