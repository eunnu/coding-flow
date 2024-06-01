from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split(" "))
number = [i for i in range(1, N+1)]
res = combinations(number, M)
for i in res:
    print(*i)