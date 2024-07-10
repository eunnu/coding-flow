from sys import stdin
inp = stdin.readline

i = 100
check = [111, 222, 333, 444, 555, 666, 777, 888, 999]
while i < 1000:
    for j in range(100, 1000):
        if i > j:
            continue
        if i in check and j in check:
            continue
        temp = float(i / j)
        a = i % 10
        na = i // 10
        b = a * 100
        if b == 0 or j//b != 1:
            continue
        nb = j % b
        if nb == 0:
            continue
        if temp == float(na/nb):
            print(i, "/", j, "=", na, "/", nb)

    i += 1

