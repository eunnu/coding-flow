for _ in range(10):
    tc = int(input())
    queue = list(map(int, input().split()))

    flag = True
    num = 1
    while flag:
        number = queue.pop(0)
        number -= num
        if number <= 0:
            number = 0
            flag = False
        queue.append(number)
        num += 1
        if num == 6:
            num = 1

    print(f"#{tc}", end=" ")
    print(*queue)
