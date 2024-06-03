from sys import stdin
from itertools import combinations_with_replacement

N, M = map(int, stdin.readline().split(" "))
num = [i for i in range(1, N + 1)]
res = combinations_with_replacement(num, M)
for i in res:
    print(*i)