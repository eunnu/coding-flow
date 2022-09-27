# 처음 달은 4가지 중에 가장 적은 비용이 드는 것으로 넣고
# 다음달 부터는 이전 달의 최저 비용과 각 경우의 수의 비용을 확인한다.
# 마지막 달이 끝나고 연간 비용과 비교하여 연간 비용이 적게 드는지 확인한다.
# 일, 달로 확인 한 dp와 월간 dp를 비교한 최종 dp와 연간 비용을 비교한다.

T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    dp = [0] * 12
    thm = [0] * 12
    dp[0] = min(price[0]*plan[0], price[1])
    for i in range(1, 12):
        dp[i] = min(price[0] * plan[i], price[1])

    for i in range(10):
        tmp = 0
        for j in range(i, i+3):
            tmp += dp[j]
            if tmp > price[2]:

                thm[j] = price[2]

    print(dp, thm)
    print(f"#{tc} {dp[11]}")



