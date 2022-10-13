# 90도 회전 -> zip 사용
# 중력은 두 번 작용한다.
# 처음부터 dfs 를 돌리면서 visit 확인 블럭 수,무지개 블럭 수, 행번호, 열번호 순으로
# 빈 칸은 9로 표기
from pprint import pprint
def gravity():
    for ux in range(N):
        tmp = []
        ydx = -1
        for uy in range(N):
            if (ydx < 0) and 0 <= board[uy][ux]:
                ydx = uy

            if ydx >= 0 and (0 <= board[uy][ux] <= 5):
                tmp.append(board[uy][ux])

            if ydx >= 0 and board[uy][ux] == -1:
                if len(tmp) >= uy:
                    ydx = -1
                    tmp.clear()
                else:
                    while len(tmp) < uy-ydx:
                        tmp = [9] + tmp

                    for yy in range(len(tmp)):
                        board[ydx+yy][ux] = tmp[yy]

                    ydx = -1
                    tmp.clear()
        if tmp:
            while len(tmp) < N-ydx:
                tmp = [9] + tmp
            for yy in range(len(tmp)):
                board[ydx+yy][ux] = tmp[yy]


def turn():
    c_board = list(map(list, zip(*board)))[::-1]
    for yi in range(N):
        for xi in range(N):
            board[yi][xi] = c_board[yi][xi]


def dfs(r, c, num):
    stack = [(r, c)]
    cnt, rainbow = 1, 0
    my, mx = 0, 0
    while stack:
        y, x = stack.pop()

        my = max(my, y)
        mx = max(mx, x)
        if (y, x) not in visit:
            visit.append((y, x))

        if board[y][x]:
            visited[y][x] = 1

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if (ny, nx) not in visit:
                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] == num or board[ny][nx] == 0:
                        stack.append((ny, nx))
                        if (ny, nx) not in visit:
                            visit.append((ny, nx))
                        if not board[ny][nx]:
                            rainbow += 1
                        cnt += 1

    flag = 0
    if maxi_num[0] <= cnt:
        if maxi_num[0] < cnt:
            flag = 1
            maxi_num[0], maxi_num[1], maxi_num[2], maxi_num[3] = cnt, rainbow, my, mx
        elif maxi_num[1] < rainbow:
            flag = 1
            maxi_num[1], maxi_num[2], maxi_num[3] = rainbow, my, mx
        elif maxi_num[2] < my:
            flag = 1
            maxi_num[2], maxi_num[3] = my, mx
        elif maxi_num[3] < mx:
            flag = 1
            maxi_num[3] = mx
        if flag:
            del_bl.clear()
            for idx in visit:
                del_bl.append(idx)

    if (cnt, rainbow, my, mx) not in block:
        block.append((cnt, rainbow, my, mx, num))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
del_bl = []
while True:
    block = []
    visited = [[0]*N for _ in range(N)]
    maxi_num = [0, 0, 0, 0]
    pprint(board)
    for i in range(N):
        for j in range(N):
            if (0 < board[i][j] <= M) and visited[i][j] == 0:
                visit = []
                dfs(i, j, board[i][j])

    if maxi_num[0] >= 2:
        ans += maxi_num[0] * maxi_num[0]

    if maxi_num[0] < 2:
        break
    for i in del_bl:
        ay, ax = i
        board[ay][ax] = 9
    pprint(board)
    del_bl.clear()
    gravity()
    pprint(board)
    turn()
    pprint(board)
    gravity()
    pprint(board)


print(ans)

