import sys

N, M = map(int, input().split(" "))
pocket = dict()
for i in range(N):
    mon = sys.stdin.readline().rstrip()
    pocket[mon] = i + 1
    pocket[str(i + 1)] = mon

for i in range(M):
    quiz = sys.stdin.readline().rstrip()
    print(pocket[quiz])