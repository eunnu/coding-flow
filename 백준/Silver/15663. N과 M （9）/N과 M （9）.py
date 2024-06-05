from sys import stdin
from itertools import permutations

N, M = map(int, stdin.readline().split(" "))
num = list(map(int, stdin.readline().split(" ")))
res = list(set(permutations(num, M)))
res.sort()
for i in res:
    print(*i)