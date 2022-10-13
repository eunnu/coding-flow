# 모든 원자들을 움직인다.
# 움직일때 겹쳤던 원자의 번호와 좌표를 넣어줌
# 4000초면 종료
# 0.5초에 만나는 경우
for tc in range(1, int(input())+1):
    N = int(input())
    c = [list(map(int, input().split())) for _ in range(N)]

    fir = dict()
    origin = dict()
    direc = [0]*N
    for i in range(N):
        origin[i] = c[i][3]
        fir[(c[i][0], c[i][1])] = [i]
        direc[i] = c[i][2]
    dy = [0.5, -0.5, 0, 0]
    dx = [0, 0, -0.5, 0.5]

    t = 0
    ans = 0
    while t < 8000:
        move = dict()
        for i in fir.keys():
            x, y = i
            n = fir[i][0]
            d = direc[n]
            x += dx[d]
            y += dy[d]

            if (x, y) in move:
                move[(x, y)].append(n)
            else:
                move[(x, y)] = [n]

        erase = []
        for i in move.keys():
            if len(move[i]) > 1:
                erase.append(i)
                for j in move[i]:
                    ans += origin[j]

        for i in erase:
            move[i].pop()
        fir = dict()
        fir.update(move)
        t += 1

    print(f"#{tc} {ans}")