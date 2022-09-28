def num(y, x, number):
    number += str(arr[y][x])
    if len(number) == 6:
        ans.add(number)
        return

    for direc in range(4):
        ny = y + dy[direc]
        nx = x + dx[direc]

        if 0 <= nx < 5 and 0 <= ny < 5:
            num(ny, nx, number)


arr = [list(map(int, input().split())) for _ in range(5)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = set()

for i in range(5):
    for j in range(5):
        num(i, j, "")

print(len(ans))