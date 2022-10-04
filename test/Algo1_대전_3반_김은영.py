# 방어탑에서 사방탐색을 통해 1을 만날 때 까지 탐색합니다.
# 공격 가능 지역은 3으로 표기하고 0의 개수를 세어줍니다.


def sol(y, x, d):
    if 0 <= y + dy[d] < N and 0 <= x + dx[d] < N:
        if area[y+dy[d]][x+dx[d]] != 1 and area[y+dy[d]][x+dx[d]] != 2:     # 진행 경로가 방어탑, 장애물이 아닌 경우
            area[y+dy[d]][x+dx[d]] = 3                                      # 공격 가능 지역으로 바꾸어줍니다.
            sol(y+dy[d], x+dx[d], d)                                        # 같은 방향으로 계속 진행해줍니다.


for tc in range(1, int(input()) + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if area[i][j] == 2:                             # 방어탑에서 시작합니다.
                for k in range(4):                          # 4방 탐색 합니다.
                    sol(i, j, k)

    ans = 0
    for i in range(N):
        for j in range(N):
            if not area[i][j]:
                ans += 1

    print(f"#{tc} {ans}")