from sys import stdin

for _ in range(int(stdin.readline())):
    N, M, x, y = map(int, stdin.readline().split(" "))
    if x == y:
        print(x)

    else:
        res = -1
        num = 0
        year, n_year = N, M
        choice, n_choice = x, y
        if N > M:
            year, n_year = M, N
            choice, n_choice = y, x
        tmp = year
        while num <= N * M:
            num += year
            tmp = num + choice
            if tmp % n_year == n_choice or (n_choice == n_year and tmp % n_year == 0):
                res = tmp
                break
        print(res)

