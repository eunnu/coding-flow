# 90도 회전 -> zip 사용
# 중력은 두 번 작용한다.
# 처음부터 dfs 를 돌리면서 visit 확인 블럭 수,무지개 블럭 수, 행번호, 열번호 순으로
# 빈 칸은 9로 표기
def gravity():       # 중력 함수
    for ux in range(N):
        tmp = []     # 내려 줄 숫자들의 리스트
        ydx = -1     # 내려 줄 숫자의 시작 인덱스
        for uy in range(N):
            if (ydx < 0) and 0 <= board[uy][ux]:       # 만약 내려줄 숫자를 만난다면 현재 인덱스를 저장
                ydx = uy

            if ydx >= 0 and (0 <= board[uy][ux] <= 5):  # 인덱스가 저장되어 있는데 숫자를 만나면 리스트에 넣어줌
                tmp.append(board[uy][ux])

            if ydx >= 0 and board[uy][ux] == -1:        # 인덱스가 존재하는데, -1을 만났다면
                if len(tmp) >= uy:                      # 리스트의 길이와 현재 인덱스가 같다면 넣어 줄 필요가 없음
                    ydx = -1                            # 인덱스와 리스트 초기화
                    tmp.clear()
                else:                                   # 리스트의 길이가 현재 인덱스보다 작은 경우
                    while len(tmp) < uy-ydx:            # 현재 위치에서 인덱스의 길이를 뺀 길이만큼
                        tmp = [9] + tmp                 # 리스트 앞 부분에 빈 칸을 넣어줌

                    for yy in range(len(tmp)):          # 저장된 인덱스 부터 해당 리스트를 기존 배열에 넣어줌
                        board[ydx+yy][ux] = tmp[yy]

                    ydx = -1
                    tmp.clear()
        if tmp:                                     # 한 행을 다 돌았는데 리스트가 존재한다면 위와 같은 행동을 반복해줌
            while len(tmp) < N-ydx:
                tmp = [9] + tmp
            for yy in range(len(tmp)):
                board[ydx+yy][ux] = tmp[yy]


def turn():        # 90 도 반시계 방향 회전
    c_board = list(map(list, zip(*board)))[::-1]
    for yi in range(N):
        for xi in range(N):
            board[yi][xi] = c_board[yi][xi]


def dfs(r, c, num):
    global my, mx
    stack = [(r, c)]
    cnt, rainbow = 1, 0
    while stack:
        y, x = stack.pop()

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
                        if board[ny][nx] == 0:
                            rainbow += 1
                        cnt += 1

    flag = 0
    # 이부분 조건 설정을 잘 못해서 맞왜틀 시전
    if maxi_num[0] <= cnt:          # 만약 그룹의 크기가 기존보다 크다면 현재 그룹 크기, 0블록 개수, y, x를 저장
        if maxi_num[0] < cnt:
            flag = 1
            maxi_num[0], maxi_num[1], maxi_num[2], maxi_num[3] = cnt, rainbow, my, mx
        else:                       # 그룹의 크기가 같다면
            if maxi_num[1] < rainbow:       # 0 블록의 개수로 확인
                flag = 1
                maxi_num[1], maxi_num[2], maxi_num[3] = rainbow, my, mx
            elif maxi_num[1] == rainbow:    # 0 블록의 개수도 같다면
                if maxi_num[2] < my:        # y 크기 비교
                    flag = 1
                    maxi_num[2], maxi_num[3] = my, mx
                elif maxi_num[2] == my:     # y도 같다면
                    if maxi_num[3] < mx:    # x 크기 비교
                        flag = 1
                        maxi_num[3] = mx
        if flag:                            # 뭔가가 변경이 있었다면
            del_bl.clear()                  # 지워야 하는 블록 인덱스의 리스트를 비워주고 다시 채워줌
            for idx in visit:
                del_bl.append(idx)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
del_bl = []
while True:

    visited = [[0]*N for _ in range(N)]
    maxi_num = [0, 0, 0, 0]
    for i in range(N):
        for j in range(N):
            if (0 < board[i][j] <= M) and visited[i][j] == 0:
                visit = [(i, j)]
                my, mx = i, j
                dfs(i, j, board[i][j])

    if maxi_num[0] >= 2:
        ans += maxi_num[0] * maxi_num[0]

    if maxi_num[0] < 2:
        break
    for i in del_bl:
        ay, ax = i
        board[ay][ax] = 9
    del_bl.clear()
    gravity()
    turn()
    gravity()

print(ans)


