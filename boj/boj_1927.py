import sys
import heapq

N = int(input())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if not num:
        if not len(heap):
            print("0")
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)