# 7bit 로 자르기 때문에 6승 부터 시작한다.

T = int(input())
for tc in range(1, T+1):
    num = input()

    d = 6
    ans = []
    tmp = 0
    for i in num:
        if d == -1:
            ans.append(tmp)
            tmp = 0
            d = 6
        if i == '1':
            tmp += (2**d)
        d -= 1

    ans.append(tmp)
    print(f"#{tc} ", end="")
    print(*ans)