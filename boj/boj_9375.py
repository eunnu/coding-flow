import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    clothes = dict()
    for _ in range(n):
        temp = sys.stdin.readline()[:-1].split(" ")
        if temp[1] not in clothes:
            clothes[temp[1]] = 1
        else:
            clothes[temp[1]] += 1

    res = 1
    for i in clothes.values():
        res *= (i + 1)

    print(res - 1)

