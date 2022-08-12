import sys
sys.stdin = open("input.txt", "r")

T = 10                                                                  # 테스트 케이스 수 : 10

dx = [-1, 1, 0]                                                         # 가로로 움직일 방향
dy = [0, 0, -1]                                                         # 세로로 움직일 방향

for _ in range(T):                                                      # 1부터 T까지 반복
    tc = int(input())                                                   # tc 번호 입력 받음

    ladder = []                                                         # 사다리 리스트

    for i in range(100):                                                # 100 줄 반복
        ladder.append(list(map(int, input().split())))                  # 줄로 입력 받음

    ans = 0                                                             # 정답을 받아 줄 변수

    y, x = 99, 0                                                        # 도착 지점 인덱스
    for i in range(100):                                                # 맨 마지막 줄 반복
        if ladder[99][i] == 2:                                          # 도착점에 도착하면
            x = i                                                       # 위치 값 받아 주기

    direc = 0                                                           # 방향 변수
    visited = [[0]*100 for _ in range(100)]                             # 방문 했는지를 확인 해줄 리스트
    visited[y][x] = 1                                                   # 도착 점 방문 했다고 표시
    while True:
        nx = x + dx[direc]                                              # 움직 일 위치 : 가로
        ny = y + dy[direc]                                              # 움직 일 위치 : 세로

        # 만약 범위 밖이거나 사다리 값이 0이거나 한번 방문 했으면 방향을 바꿔줌
        if nx < 0 or ny < 0 or nx > 99 or ny > 99 or ladder[ny][nx] == 0 or visited[ny][nx]:
            direc += 1
            direc %= 3
            continue

        if ny == 0 and ladder[ny][nx]:                                   # 만약 출발 점이면
            ans = nx                                                     # 해당 x 좌표를 답 변수에 넣어줌
            break                                                        # 반복 문 종료

        x = nx                                                           # 원래 위치에 이동한 x 좌표를 넣어줌
        y = ny                                                           # 원래 위치에 이동한 y 좌표를 넣어줌
        visited[ny][nx] = 1                                              # 현재 방문한 위치 표시

        if direc < 2:                                                    # 만약 오른쪽, 왼쪽으로 꺾었다면
            direc = 0                                                    # 방향 값 초기화
            continue

        direc += 1                                                       # 방향 바꿔주고
        direc %= 3                                                       # 방향은 3으로 나눈 나머지 값

    print(f"#{tc} {ans}")                                                # 결과 출력
