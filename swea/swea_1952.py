# 어짜피 1,2일을 해도 3일을 하는게 이득임
T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))

    first = [0] * 12
    for i in range(12):
        first[i] = min(price[0]*month[i], price[1])
    print(first)
    ans = []
    for i in range(12):
        tmp = []
        s = 0
        cnt = 0
        for j in range(i, 12):
            cnt += 1
            s += first[j]
            if cnt == 3:
                cnt = 0
                s = 0
                if s <= first[j]:
                    tmp.pop()
                    tmp.pop()
                    tmp.append(price[2])
            tmp.append(first[j])
        if sum(tmp) < price[-1] and sum(tmp):
            ans.append(sum(tmp))
    ans.append(sum(first))

    print(ans)




