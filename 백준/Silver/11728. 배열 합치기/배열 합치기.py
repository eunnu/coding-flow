from sys import stdin

inp = stdin.readline
N, M = map(int, inp().split(" "))
A = list(map(int, inp().split(" ")))
B = list(map(int, inp().split(" ")))
C = list(A + B)
C = sorted(C)
print(*C)