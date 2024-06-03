from sys import stdin
from itertools import permutations

N, M = map(int, stdin.readline().split(" "))
num = list(map(int, stdin.readline().split(" ")))
num.sort()
res = permutations(num, M)
for i in res:
    print(*i)