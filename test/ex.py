def min_sum(depth, acc):
    global minS

    if acc > minS:
        return

    if depth == N:
        if acc < minS:
            minS = acc
        return

    arr = mat[depth]
    for i in range(N):
        if not check[i]:
            acc += arr[i]
            check[i] = 1
            min_sum(depth + 1, acc)
            check[i] = 0
            acc -= arr[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    check = [0]*N
    sel =[0]*N
    minS = 999999999

    min_sum(0, 0)

    print(f'#{tc} {minS}')