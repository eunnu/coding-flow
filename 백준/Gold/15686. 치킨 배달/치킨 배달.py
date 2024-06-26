from sys import stdin

inp = stdin.readline
N, M = map(int, inp().split(" "))
chicken = []
house = []


def sol(arr):
    result = 987654321
    for ch in arr:
        res = 0
        for h in house:
            cnt = float('inf')
            for c in ch:
                d = chicken[c]
                temp = abs(d[0] - h[0]) + abs(d[1] - h[1])
                if cnt > temp:
                    cnt = temp
            res += cnt
            if res > result:
                break
        if result > res:
            result = res
    print(result)


def comb(arr, num):
    res = []
    if not num:
        return [[]]

    for k in range(0, len(arr)):
        elem = arr[k]
        rest_arr = arr[k+1:]
        for m in comb(rest_arr, num-1):
            res.append([elem]+m)

    return res


for i in range(N):
    tmp = list(map(int, inp().split(" ")))
    for j in range(N):
        if tmp[j] == 1:
            house.append([i, j])
        elif tmp[j] == 2:
            chicken.append([i, j])

r = comb([i for i in range(len(chicken))], M)

sol(r)
