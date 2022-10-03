def check(idx, money):
    global ans
    if money > ans:
        return

    if idx >= len(brr):
        return

    if len(visited) == 3:
        if ans > money:
            ans = money
        return

    else:
        y, x = brr[idx][1], brr[idx][2]
        if [y, x] not in visited:
            for jdx in visited:
                if abs(jdx[0] - y) and abs(jdx[1]-x):
                    visited.append([y, x])
                    check(idx+1, money+brr[idx][0])
                    visited.remove([y, x])
                elif abs(jdx[0] - y) == 1 or abs(jdx[1] - x) == 1:
                    check(idx+1, money)
                elif not abs(jdx[0] - y) and not abs(jdx[1] - x):
                    check(idx+1, money)
                else:
                    visited.append([y, x])
                    check(idx+1, money+brr[idx][0])
                    visited.remove([y, x])


N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

brr = []
for i in range(1, N-1):
    for j in range(1, N-1):
        sum_arr = area[i][j]
        for direc in range(4):
            sum_arr += area[i+dy[direc]][j+dx[direc]]
        brr.append([sum_arr, i, j])

brr.sort()
print(brr)
ans = 987654321
for i in range(len(brr)):
    tmp = brr[i][0]
    visited = [[brr[i][1], brr[i][2]]]
    check(i+1, tmp)

print(ans)