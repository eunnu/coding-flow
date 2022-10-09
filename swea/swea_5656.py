# 시뮬
# 가장 높이 있는 벽돌들을 stack 에 넣어 놓고 벽돌을 깬다.
def drop():                                                                 # 벽돌 내리는 함수
    pass


def sol(y, x):                                                              # 벽돌 깨는 함수
    pass


for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())

    li = [list(map(int, input().split())) for _ in range(H)]

    top_q = []
    for i in range(H):
        if 1 in li[i]:
            for j in range(W):
                if li[i][j]:
                    top_q.append([i, j, li[i][j]])

            break

    ans = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while top_q:
        r, c, num = top_q.pop()
        stack = []

