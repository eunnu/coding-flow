def sol(idx, money):
    global ans
    if idx == len(brr):
        return

    if len(visited) == 3:
        if ans > money:
            ans = money
        return

    else:
        y, x = brr[idx][1], brr[idx][2]
        check = set()
        for jdx in visited:
            for kdx in range(4):
                check.add((jdx[0] + dy[kdx], jdx[1] + dx[kdx]))

        if (y, x) not in check:
            flag = False
            for jdx in range(4):
                if (y+dy[jdx], x+dx[jdx]) in check:
                    flag = True
                    break
            if not flag:
                visited.append([y, x])
                sol(idx+1, money+brr[idx][0])
                visited.remove([y, x])
            else:
                sol(idx+1, money)

        else:
            sol(idx+1, money)


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

ans = 3000
for i in range(len(brr)-1):
    tmp = brr[i][0]
    visited = [[brr[i][1], brr[i][2]]]
    sol(i+1, tmp)

print(ans)