N, K = map(int, input().split(" "))
stick_len = list()
for _ in range(N):
    stick_len.append(int(input()))
start, end = 1, max(stick_len)

num = 0
result = 0
while start <= end:
    num = 0
    mid = (start + end) // 2

    for i in stick_len:
        num += i // mid

    if num < K:
        end = mid - 1

    else:
        start = mid + 1
        result = max(result, mid)

print(result)


