'''
첫 줄과 마지막 줄은 무조건 흰색과 빨강이어야 함
파랑 줄도 무조건 한 줄이 주어져야 함.
N 개의 줄이기 때문에 N개의 줄에 벽을 2개 칠거임
근데 그 두 개의 벽이 겹치면 안됨
첫 벽은 무조건 1 띄워서 놔야 하고 마지막 벽은 무조건 한 개 남겨 놔야 함
그렇기 때문에 범위가 1 ~ N -> i // i + 1 ~ N -> j
각 줄 마다 자신이 아닌 색의 개수를 카운트해서 리스트에 넣어놓고, 본인의 구역의 값을 더해줌
최소값을 업데이트
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    w = [0]*N                                       # 흰색
    r = [0]*N                                       # 빨강
    b = [0]*N                                       # 파랑
    for i in range(N):
        arr.append(list(map(str, input())))
        for j in range(M):
            if arr[i][j] != 'W':                    # 흰색이 아닌 경우 몇 개 칠해야 하는지
                w[i] += 1
            if arr[i][j] != 'B':                    # 파랑이 아닌 경우 몇 개?
                b[i] += 1
            if arr[i][j] != 'R':                    # 빨강이 아닌 경우 몇 개?
                r[i] += 1

    ans = 987654321

    for i in range(1, N):                                       # 첫 번째 벽의 위치
        for j in range(i+1, N):                                 # 두 번째 벽의 위치
            tmp = sum(w[:i]) + sum(b[i:j]) + sum(r[j:N+1])      # 그 구역에서 몇 개의 색을 칠해야 하는지 더해서
            if tmp < ans:                                       # 최소값 업데이트
                ans = tmp

    print(f"#{tc} {ans}")