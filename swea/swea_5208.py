# 재귀, 백트래킹
# 과연 전기버스 1보다 발전했을 것인가
def gogo(depth, b, cnt):
    global ans
    if cnt > ans:
        return

    if b < 0:
        return

    if depth == bus[0]:
        if cnt < ans:
            ans = cnt
        return

    else:
        if depth+1 not in visit or visit[depth+1] > cnt + 1:
            visit[depth+1] = cnt + 1
            gogo(depth + 1, b + bus[depth] - 1, cnt + 1)
        gogo(depth + 1, b - 1, cnt)


T = int(input())
for tc in range(1, T+1):
    bus = list(map(int, input().split()))
    ans = bus[0]
    visit = dict()
    visit[1] = 0
    gogo(2, bus[1] - 1, 0)

    print(f"#{tc} {ans}")