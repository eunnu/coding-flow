from sys import stdin

A, B, C = map(int, stdin.readline().split(" "))
res = 1
while B:
    if B & 1:
        res *= A
    A *= A
    A = A%C
    B = B >> 1
print(res%C)