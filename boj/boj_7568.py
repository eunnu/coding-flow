import sys

N = int(sys.stdin.readline())
people = []
res = []
for _ in range(N):
    people.append(list(map(int, sys.stdin.readline().split(" "))))

for i in range(N):
    x, y = people[i]
    x_cnt, y_cnt = 0, 0
    for j in range(N):
        dx, dy = people[j]
        if people[j] == [x, y]:
            continue

        if x < dx:
            x_cnt += 1
            if y < dy:
                y_cnt += 1
    res.append(min(x_cnt, y_cnt) + 1)

print(*res)
