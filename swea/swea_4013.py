# 홀수번끼리 짝수번끼리 움직이는 방향과 확인해 주어야 하는 번호가 같다.
# 움직이는 자석의 양 옆으로 뻗어나가면서 움직여야 하는 자석을 체크하고 동시에 움직여 준다.
# 다 움직인 후에 점수를 확인한다.
def sol(num, tmp, m):
    if 0 <= num <= 3:
        if not visit[num]:
            if ns[num][m] != tmp:
                move[num] = 1
                visit[num] = 1
                sol(num - 1, ns[num][6], 2)
                sol(num + 1, ns[num][2], 6)


def turn(n, d):
    if 0 <= n <= 3:
        if move[n]:
            if not visit[n]:
                visit[n] = 1
                if d == 1:
                    tmp = ns[n].pop()
                    ns[n] = [tmp] + ns[n]
                    turn(n+1, -1)
                    turn(n-1, -1)
                else:
                    tmp = ns[n].pop(0)
                    ns[n].append(tmp)
                    turn(n+1, 1)
                    turn(n-1, 1)


# T = int(input())
# for tc in range(1, T+1):
ns = [list(map(int, list(input()))) for _ in range(4)]
K = int(input())            # 회전 수
for i in range(K):
    No, direction = map(int, input().split())
    move = [0]*4
    visit = [0]*4
    move[No-1] = 1
    visit[No-1] = 1
    sol(No - 1 - 1, ns[No-1][6], 2)
    sol(No, ns[No-1][2], 6)
    visit = [0]*4
    turn(No - 1, direction)

ans = 0
for i in range(4):
    ans += ns[i][0] * (2**i)

print(ans)