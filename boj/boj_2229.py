from pprint import pprint

N = int(input())

li = list(map(int, input().split()))

arr = [[0]*N for _ in range(N)]

for i in range(N):
    maxi, mini = -1, 987654321
    for j in range(i, N):
        maxi = max(maxi, li[j])
        mini = min(mini, li[j])
        arr[i][j] = maxi - mini
# 2 5 7 1 3 4 8 6 9 3 을 예시로 각 숫자별 묶음 갯수 별 가장 큰 차이를 넣어줌
# [[0, 3, 5, 6, 6, 6, 7, 7, 8, 8],
#  [0, 0, 2, 6, 6, 6, 7, 7, 8, 8],
#  [0, 0, 0, 6, 6, 6, 7, 7, 8, 8],
#  [0, 0, 0, 0, 2, 3, 7, 7, 8, 8],
#  [0, 0, 0, 0, 0, 1, 5, 5, 6, 6],
#  [0, 0, 0, 0, 0, 0, 4, 4, 5, 6],
#  [0, 0, 0, 0, 0, 0, 0, 2, 3, 6],
#  [0, 0, 0, 0, 0, 0, 0, 0, 3, 6],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

dp = [0]*N
# dp 배열을 만들어 줌

for i in range(N):                                          # 이거는 몇 번째 숫자
    for j in range(i):                                      # 몇 번 째 묶음
        dp[i] = max(dp[j] + arr[j+1][i], dp[i])             # 현재 몇번 째 숫자를 어떤 묶음으로 묶는게 가장 큰 값인지 비교
    dp[i] = max(arr[0][i], dp[i-1], dp[i])                  # 초기 값과 이전 수의 묶음과 현재 수의 묶음중에 가장 큰 묶음으로 가져옴
print(dp[N-1])
