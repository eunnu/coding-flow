# N/2 개를 추출하는 함수를 만들고
# N/2 개를 추출하면 남은 것과 함께 시너지를 계산해 줄 함수로 전달
# 더해서 최소 값을 구해줌
# 소요시간 : 1시간


def sol(check, n_check):

    ch, nch = 0, 0
    for j in range(N//2-1):
        for k in range(j+1, N//2):
            ch += food[check[j]][check[k]] + food[check[k]][check[j]]                   # 첫번째 손님
            nch += food[n_check[j]][n_check[k]] + food[n_check[k]][n_check[j]]          # 두번째 손님

    res = abs(ch - nch)
    return res


def comb(depth, dx):
    global ans
    if depth == N//2:
        one = []
        two = []
        for idx in range(N):
            if visited[idx]:
                one.append(idx)
            else:
                two.append(idx)
        res = sol(one, two)
        if res < ans:
            ans = res
        return

    else:
        for i in range(dx, N):                          # 이 범위가 중요
            if not visited[i]:                          # 조합
                visited[i] = 1
                comb(depth+1, i + 1)
                visited[i] = 0
    return


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    ans = 987654321
    comb(0, 0)

    print(f"#{tc} {ans}")


