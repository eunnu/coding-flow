def n_queen(y, x, visit):
    global res
    if queen == N - 1:
        res += 1
        return

    else:



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]

    queen = 1
    res = 0
    n_queen(0, 0, board)
    print(f"#{tc} {res}")