def change(number):
    global ans
    tmp = ""
    while number > 0:
        tmp = str(number % 2) + tmp
        number //= 2

    if len(tmp) < 4:
        while len(tmp) < 4:
            tmp = "0" + tmp

    ans += tmp


T = int(input())
for tc in range(1, T+1):
    M, num = input().split()

    li = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    ans = ""
    for i in num:
        if i in li:
            change(li[i])
        else:
            change(int(i))

    print(f"#{tc} {ans}")