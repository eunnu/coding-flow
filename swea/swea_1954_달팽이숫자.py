T = int(input())                                                            # 테스트케이스 수 입력 받음

dx = [1, 0, -1, 0]                                                          # 가로 방향 인덱스 : 좌    우
dy = [0, 1, 0, -1]                                                          # 세로 방향 인덱스 :    하     상
for tc in range(1, T+1):                                                    # 테스트 케이스 수 만큼 반복
    snail_num = []                                                          # 달팽이 숫자 리스트 선언
    n = int(input())                                                        # 숫자의 크기를 입력 받음
    for i in range(n):                                                      # 숫자의 크기 만큼 반복
        snail_num.append([])                                                # 2차원 배열로 만들어 줌
        for j in range(n):                                                  # n 만큼 반복
            snail_num[i].append(0)                                          # 2차원 배열을 0으로 초기화

    maxi = n * n                                                            # 최대 숫자는 n * n
    x, y, snail_dir, input_num = 0, 0, 0, 2                                 # 처음 달팽이의 위치는 0,0 방향 0, 처음에 1을 넣어 주기 때문에
    snail_num[0][0] = 1                                                     # 처음 달팽이의 위치에 시작 num 1을 넣어줌

    while input_num <= maxi:                                                # 넣어주는 숫자가 최대 숫자와 같아질 때 까지 반복
        nx = x + dx[snail_dir]                                              # 달팽이가 움직일 가로 위치는 현재 x + x축 방향
        ny = y + dy[snail_dir]                                              # 달팽이가 움직일 가로 위치는 현재 y + y축 방향
        if nx < 0 or ny < 0 or nx >= n or ny >= n or snail_num[ny][nx]:     # 만약 움직일 위치가 배열 밖이거나, 0이 아니라면
            snail_dir += 1                                                  # 움직일 방향을 바꿔주고
            if snail_dir == 4:                                              # 바꿨는데 만약 방향이 4라면
                snail_dir = 0                                               # 다시 0으로 초기화
            continue                                                        # 숫자를 넣어주지 않고 처음으로 돌아감

        snail_num[ny][nx] = input_num                                       # 움직일 위치가 범위 내 면서 0이라면 숫자를 넣어줌
        input_num += 1                                                      # 넣어 줄 숫자를 1 더해줌
        x, y = nx, ny                                                       # 현재 위치에 움직인 위치를 넣어줌

    print(f"#{tc}")                                                         # 테스트 케이스 번호 출력
    for i in range(n):                                                      # 현재 배열의 크기 만큼
        for j in range(n):                                                  # 이차원배열이니 두번 반복
            print(snail_num[i][j], end=' ')                                 # 가로 줄을 출력하고
        print()                                                             # 줄 바꿈

