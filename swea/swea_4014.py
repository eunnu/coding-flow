# 1. 지면의 차이가 2 이상인 경우 break
# 2. 지면의 길이가 경사로의 길이 보다 짧은 경우 break
def check_c(y):
    # 리턴 할 때 마다 ans + 1 해줄 거임 왜냐면 돌아가는건 불가능 하단 거기 때문에 어쨋던 한 턴에 한번이란 뜻
    global ans
    flag = False
    c = 0
    while c < N-1:
        if abs(ground[y][c] - ground[y][c+1]) > 1:
            ans += 1
            return

        if ground[y][c] < ground[y][c+1]:       # 오르막길
            c += 1
            if c-X < 0:
                ans += 1
                return
            for cnt in range(1, X):
                if ground[y][c - cnt] != ground[y][c - cnt - 1]:
                    flag = True
                    break
                else:
                    if not visit[c-cnt]:
                        visit[c - cnt] = 1
                    else:
                        flag = True
                        break

            if not visit[c - X]:
                visit[c-X] = 1
            else:
                ans += 1
                return
            continue

        elif ground[y][c] > ground[y][c+1]:       # 내리막길
            c += 1
            if c+X-1 >= N:
                ans += 1
                return
            for cnt in range(X-1):
                if ground[y][c + cnt] != ground[y][c + cnt + 1]:
                    flag = True
                    break
                else:
                    if not visit[c + cnt]:
                        visit[c + cnt] = 1
                    else:
                        flag = True
                        break

            if flag:
                ans += 1
                return
            if not visit[c+X-1]:
                visit[c+X-1] = 1
            else:
                ans += 1
                return

            c += X-2
            continue

        if flag:
            ans += 1
            return

        c += 1


def check_r(x):
    global ans
    global ans
    flag = False
    c = 0
    while c < N-1:
        if abs(ground[c][x] - ground[c + 1][x]) > 1:
            ans += 1
            return

        if ground[c][x] < ground[c + 1][x]:  # 오르막길
            c += 1
            if c-X < 0:
                ans += 1
                return
            for cnt in range(1, X):
                if ground[c - cnt][x] != ground[c - cnt - 1][x]:
                    flag = True
                    break
                else:
                    if not visit[c - cnt]:
                        visit[c - cnt] = 1
                    else:
                        flag = True
                        break

            if not visit[c - X]:
                visit[c - X] = 1
            else:
                ans += 1
                return
            continue

        elif ground[c][x] > ground[c + 1][x]:  # 내리막길
            c += 1
            if c+X-1 >= N:
                ans += 1
                return
            for cnt in range(X-1):
                if ground[c + cnt][x] != ground[c + cnt + 1][x]:
                    flag = True
                    break
                else:
                    if not visit[c + cnt]:
                        visit[c + cnt] = 1
                    else:
                        flag = True
                        break
            if flag:
                ans += 1
                return
            if not visit[c + X-1]:
                visit[c + X-1] = 1
            else:
                ans += 1
                return

            c += X-2
            continue

        if flag:
            ans += 1
            return

        c += 1


for tc in range(1, int(input())+1):
    N, X = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        visit = [0]*N
        check_c(i)
        # print("가로", i, ans)

        visit = [0]*N
        check_r(i)
        # print("세로", i, ans)
    print(f"#{tc} {N+N - ans}")


