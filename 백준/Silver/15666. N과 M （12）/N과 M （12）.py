from sys import stdin
from itertools import combinations_with_replacement

N, M = map(int, stdin.readline().split(" "))
num = list(map(int, stdin.readline().split(" ")))
num.sort()
res = list(set(combinations_with_replacement(num, M)))
res.sort()
for i in res:
    print(*i)
