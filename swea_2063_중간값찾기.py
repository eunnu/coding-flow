n = int(input())

arr = list(map(int, input().split()))

arr.sort()

mid = (int)(n/2)
print(arr[mid])