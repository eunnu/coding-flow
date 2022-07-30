T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split(' ')))

    money = 0

    while True:
        if li == []: break
        cnt, buy = 0
        max_money = max(li)
        idx = 0
        for i in range(len(li)):
            if li[i] == max_money:
                money = (max_money * cnt - buy) + money
                idx = i
                print(max_money, cnt, buy,money, i)
                cnt = 0
                buy = 0
            else:
                cnt += 1
                buy += li[i]

        del li[:idx+1]
    
    print(f'#{tc} {money}')