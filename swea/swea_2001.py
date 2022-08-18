T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    area = []
    for i in range(N):
        area.append(list(map(int, input().split())))

    i, j, ans = 0, 0, 0
    while True:
        die = 0
        for g in range(M):
            for f in range(M):
                if i+f >= N or j+g >= N or i+f < 0 or j+g < 0:
                    continue
                die += area[i+g][j+f]

        i += 1
        if i > N-M:
            j += 1
            i = 0
        if ans < die:
            ans = die
        if j > N - M:
            break

    print(f"#{tc} {ans}")