import heapq
from sys import stdin

q = []
for _ in range(int(stdin.readline())):
    num = int(stdin.readline())
    if num == 0 and not q:
        print(0)
    elif num == 0 and q:
        print(heapq.heappop(q)[1])
    elif num != 0:
        heapq.heappush(q, (abs(num), num))