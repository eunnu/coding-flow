N, M = map(int, input().split(" "))

res = 0
t = 987654321
for i in range(1, N+1):
    l, s = map(int, input().split(" "))
    temp = (M-l)/s
    if t > temp:
        res = i
        t = temp

print(res)