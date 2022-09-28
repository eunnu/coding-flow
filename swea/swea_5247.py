# BFS 로 푸는데 백트래킹이 관건이다.
# 오늘은 과연 풀 것인가
from collections import deque

T = int(input())
for tc in range(1, T+1):
    start, end = map(int, input().split())

    queue = deque()
    queue.append((start, 0))
    visited = set()
    ans = end - start + 1

    while queue:
        (num, cnt) = queue.popleft()

        if num in visited:
            continue

        visited.add(num)

        if num == end:
            if ans > cnt:
                ans = cnt
            break

        if 0 < num*2 < 1000000 and num*2 not in visited:
            queue.append((num*2, cnt + 1))

        if num+1 not in visited:
            queue.append((num+1, cnt + 1))

        if 0 < num-1 and num-1 not in visited:
            queue.append((num-1, cnt + 1))

        if 0 < num - 10 and num - 10 not in visited:
            queue.append((num-10, cnt + 1))

    print(f"#{tc} {ans}")

