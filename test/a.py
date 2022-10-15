for tc in range(1, int(input()) + 1):
    N = int(input())
    tree = list(map(int, input().split()))

    tree.sort()
    tall = tree[-1]
    ans = 987654321
    cnt = 0

    jack = []
    hall = []
    for i in range(N - 1):
        num = tall - tree[i]
        if num % 2:
            hall.append(1)
            num -= 1
        num //= 2
        while num > 0:
            jack.append(2)
            num -= 1

    if jack:
        if not hall:
            jack.pop()
            hall.append(1)
            hall.append(1)
    flag = False
    if jack:
        while jack:
            jack.pop()
            hall.pop()
            cnt += 2

            if not hall and jack:
                jack.pop()
                flag = not flag
                hall.append(1)
                hall.append(1)

    # if hall:
    #     hall.pop()
    #     if flag:
    #         cnt += 2
    #     else:
    #         cnt += 1
    #
    if hall:
        while hall:
            hall.pop()
            cnt += 2

    print(f"#{tc} {cnt}")