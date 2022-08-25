T = int(input())
for tc in range(1, T+1):
    N, num = map(int, input().split())
    queue = list(map(int, input().split()))
    ans = 0
    while num > 0:
        queue.append(queue.pop(0))
        num -= 1
        if num == 0:
            ans = queue[0]
    print(f"#{tc} {ans}")