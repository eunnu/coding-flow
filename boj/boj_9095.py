from collections import deque


N = int(input())
number = [1, 2, 3]
for _ in range(N):
    num = int(input())
    queue = deque()
    for i in number:
        queue.append(i)
    ans = 0
    while queue:
        a = queue.popleft()
        if a == num:
            ans += 1
        for i in number:
            if a + i == num:
                ans += 1
            elif a + i < num:
                queue.append(a+i)

    print(ans)