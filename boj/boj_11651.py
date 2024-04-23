import sys

N = int(sys.stdin.readline())

sol = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split(" "))
    sol.append((x, y))

sol = sorted(sol, key=lambda a: (a[1], a[0]))
for i in sol:
    print(*i)