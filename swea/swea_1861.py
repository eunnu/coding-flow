# 전체 맵을 돌면서 dfs 를 도는데 최대 값이 현재 시작하는 방 번호보다 크다면 종료
# 예를 들어, n이 9 인데 max 값이 6이고 현재 시작 방 번호가 4 라면 확인 해 줄 필요가 없음
# 새로운 배열을 만들어 현재 위치의 최대값보다 현재 cnt 작다면 반환

def dfs(y, x):
    global tmp
    for dire in range(4):
        ny = y + dy[dire]
        nx = x + dx[dire]

        if 0 <= nx < N and 0 <= ny < N:
            if (ny, nx) not in visited:
                if room[ny][nx] == room[y][x] + 1:
                    if tmp + 1 > move[ny][nx]:
                        visited.add((ny, nx))
                        move[ny][nx] = tmp + 1
                        tmp += 1
                        dfs(ny, nx)
                    else:
                        return
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    ans = [0, 0]
    move = [[0]*N for _ in range(N)]

    flag = False
    for i in range(N):
        for j in range(N):
            tmp = 1
            visited = set()
            dfs(i, j)
            if tmp > ans[1]:
                ans[1] = tmp
                ans[0] = room[i][j]
            elif tmp == ans[1]:
                if ans[0] > room[i][j]:
                    ans[0] = room[i][j]

    print(f"#{tc} {ans[0]} {ans[1]}")