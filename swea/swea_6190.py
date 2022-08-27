def num_sort(num):
    global result
    a = num % 10
    num //= 10
    while num != 0:
        b = num % 10
        num //= 10
        if a < b:
            return - 1
        a = b

    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    result = -1
    for i in range(N - 1):
        for j in range(i+1, N):
            tmp = number[i]*number[j]
            if tmp < 10:
                continue
            elif tmp < result:
                continue
            else:
                ans = num_sort(tmp)
                if not ans and tmp > result:
                    result = tmp

    print(f"#{tc} {result}")

    '''
    5
3
1 1 1
4
1 1 13 1
4
2 4 7 10
10
1 2 3 4 5 6 7 8 9 10
4
1 1 13 19
    '''