import sys

N = int(sys.stdin.readline())
res = 0
for num in range(1, N + 1):
    temp = num
    i = num
    while i > 0:
        temp += (i % 10)
        i = i // 10
    if temp == N:
        res = num
        break
print(res)