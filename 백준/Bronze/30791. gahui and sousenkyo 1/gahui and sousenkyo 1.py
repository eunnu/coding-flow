from sys import stdin

characters = list(map(int, stdin.readline().split(" ")))
top_16 = characters[0]
res = 0
for i in range(1, 5):
    if top_16 - characters[i] <= 1000:
        res += 1
    else:
        break

print(res)