'''
bfs로 풀거임
근데 이제 사탕 크기를 같이 넣어 줄 거임
그럴 거임 -> 시간 초과가 너무 나는 관계로.. 풀이 방법 변경.. dp 인데 이제 이차원..
이 문제 같은 경우에는 무조건 가로나 세로로 움직이는 경로가 제일 좋음
현재 인덱스의 가장 큰 값 같은 경우는 가로 전 인덱스인 maze[y][x-1] 과 세로 전 인덱스인 maze[y-1][x] 중 큰 값과 현재 인덱스의 값임
'''

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        dp[i][j] += maze[i][j]
print(dp[N-1][M-1])