# 1. 제일 낮은 층에 맞추는 것 : 256 초과시 아웃
# 2. 제일 높은 층에 맞추는 것 : B 개수보다 낮은 층이 많으면 아웃
# 3. 중간 층에 맞추는 것 : 가장 낮은 것과 높은 것의 중간을 구하고 그 층에 맞춤.
#    해당 과정을 아웃 되지 않는 선에서 반복할 것


import sys

N, M, B = map(int, sys.stdin.readline().split(" "))
mine = []
min_n, max_n = 987654321, 0
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split(" ")))
    min_n = min(min_n, temp)
    max_n = max(max_n, temp)
    mine.append(temp)


