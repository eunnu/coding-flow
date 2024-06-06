from sys import stdin

N = int(stdin.readline())
shirt = list(map(int, stdin.readline().split(" ")))
t, p = map(int, stdin.readline().split(" "))
res = 0
for i in shirt:
    if i == 0:
        continue
    if i % t:
        res += i // t + 1
    else:
        res += i // t

print(res)
print(N // p, N % p)