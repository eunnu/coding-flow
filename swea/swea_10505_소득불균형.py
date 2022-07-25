T = int(input())

for test in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
   
    sum_num = 0
    for i in range(n):
        sum_num += arr[i]
    mid = sum_num//n
    cnt = 0

    sorted(arr)
    for i in arr:
        if i <= mid:
            cnt += 1

    print('#%d %d'%(test+1, cnt))

