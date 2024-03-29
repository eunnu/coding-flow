N = int(input())
A = list(map(int, input().split(" ")))
M = int(input())
B = list(map(int, input().split(" ")))

# A 정렬 후 이분탐색 할 것
A.sort()

for i in B:
    start, end = 0, N - 1
    while True:
        mid = (start + end) // 2
        if A[mid] == i:
            print("1")
            break
        if start >= end:
            print("0")
            break

        elif A[mid] <= i:
            start = mid + 1

        elif A[mid] > i:
            end = mid - 1

