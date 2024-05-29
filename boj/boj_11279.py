import heapq
import sys

heap = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if heap and num == 0:
        print(-heapq.heappop(heap))
    elif num != 0:
        heapq.heappush(heap, -num)
    elif not heap:
        print(0)