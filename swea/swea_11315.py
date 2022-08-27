'''
가로 세로를 확인 해 줄 함수 하나
대각선, 역대각선 확인 해 줄 함수 하나
인덱스를 계산해서 범위를 넘으면 돌지 않는 걸로
'''


def xy(y, x):                                           # 가로 세로를 확인 해 줄 함수
    x_cnt, y_cnt = 0, 0
    for idx in range(5):
        if (x+4) < N and Om[y][x + idx] == 'o':         # 인덱스를 넘지 않는 범위 내에서 가로 카운트
            x_cnt += 1
        if (y+4) < N and Om[y+idx][x] == 'o':           # 인덱스를 넘지 않는 범위 내에서 세로 카운트
            y_cnt += 1

    if y_cnt >= 5 or x_cnt >= 5:                        # 가로 혹은 세로의 오목 개수가 5 이상이면 1을 반환
        return 1
    else:
        return 0


def sr(y, x):
    s_cnt, r_cnt = 0, 0
    for idx in range(5):
        if (x+4) < N and (y+4) < N and Om[y+idx][x+idx] == 'o':     # 인덱스를 넘지 않는 범위 내에서 대각선 카운트
            s_cnt += 1
        if 0 <= (x-4) and (y+4) < N and Om[y+idx][x-idx] == 'o':    # 인덱스를 넘지 않는 범위 내에서 역 대각선 카운트
            r_cnt += 1

    if s_cnt >= 5 or r_cnt >= 5:                                    # 대각, 역 대각 개수가 5 이상이면 1 반환
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Om = []
    for i in range(N):
        Om.append(list(input()))

    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if Om[i][j] == 'o':
                res = xy(i, j)
                if res:
                    ans = 'YES'
                res = sr(i, j)
                if res:
                    ans = 'YES'
    print(f"#{tc} {ans}")