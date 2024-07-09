# 사용한 알고리즘 : union find
from sys import stdin


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y, mem):
    rootx = find(parent, x)
    rooty = find(parent, y)

    if rootx in mem and rooty in mem:
        return

    if rootx in mem:
        parent[rooty] = rootx
    elif rooty in mem:
        parent[rootx] = rooty
    else:
        if rootx < rooty:
            parent[rooty] = rootx
        else:
            parent[rootx] = rooty


N, M = map(int, stdin.readline().split(" "))
K = list(map(int, stdin.readline().split(" ")))[1:]
parent = [i for i in range(N + 1)]
L = []

for i in range(M):
    temp = list(map(int, stdin.readline().split(" ")))
    people = temp[1:]

    for j in range(temp[0] - 1):
        union(parent, people[j], people[j+1], K)
    L.append(temp[1:])

res = 0
for i in L:
    for j in range(len(i)):
        if find(parent, i[j]) in K:
            break
    else:
        res += 1
print(res)