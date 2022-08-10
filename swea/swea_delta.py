T = int(input())                                        # 테스트케이스 수를 입력받음

for tc in range(1, T + 1):                              # 테스트 케이스 변수 tc를 1부터 T까지 반복

    def abs_xy(a, b):                                   # 절대값 차 구하는 함수
        if a < b:                                       # a가 b보다 작으면
            return b-a                                  # b - a를 반환
        else:                                           # b가 a보다 작으면
            return a-b                                  # a - b를 반환

    N = int(input())                                    # 배열의 크기를 입력 받음

    arr = []                                            # arr 리스트 선언
    for i in range(N):                                  # N줄을 받기 위해 N 만큼 반복
        arr.append(list(map(int, input().split())))     # 한 줄씩 입력 받음

    dx = [0, 0, -1, 1]                                  # 좌 우
    dy = [1, -1, 0, 0]                                  # 상 하 로 움직여 줄 델타 리스트 선언
    x, y, sum_arr = 0, 0, 0                             # 현재 위치를 알려줄 x, y 전체 합을 구해줄 변수 선언

    while True:                                         # 반복문 시작
        sum_idx = 0                                     # 현재 위치에서 이웃한 배열과의 차의 합을 구하기 위한 변수
        for k in range(4):                              # 4 방향 만큼 반복
            nx = x + dx[k]                              # 현재 위치에서 가로로 움직일 방향
            ny = y + dy[k]                              # 현재 위치에서 세로로 움직일 방향

            if nx < 0 or ny < 0 or nx >= N or ny >= N:  # 만약 배열 범위 밖으로 나간다면
                continue                                # continue
            sum_idx += abs_xy(arr[y][x], arr[ny][nx])   # 이웃한 배열과의 차의 합을 구하기 위해 차를 구해줄 함수에 현 위치와 움직인 위치값을 보내줌

        sum_arr += sum_idx                              # 전체 합에 이웃한 배열과의 합을 더해줌
        x += 1                                          # 오른쪽으로 이동
        if x == N:                                      # 오른쪽 끝을 벗어나면
            y += 1                                      # 아래줄
            x = 0                                       # 맨 왼쪽으로 이동

        if y == N:                                      # 아랫줄을 벗어나면
            break                                       # 반복 종료

    print(f"#{tc} {sum_arr}")                           # 결과 출력
