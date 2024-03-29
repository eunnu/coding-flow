import sys


# 더이상 나눌 수 없을 때까지 나누어 주어야 함.
# 가장 큰 곳에서 1사분면을 먼저 살펴서 작은 구역으로 들어가서 return


N = int(input())

card = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]

