# while True:
#     triangle = list(map(int, input().split()))
#     if sum(triangle) == 0:
#         break
#     triangle.sort()
#     if triangle[0]**2 + triangle[1]**2 == triangle[-1]**2:
#         print("right")
#     else:
#         print("wrong")

# N = int(input())
# age = list()
# for _ in range(N):
#     a, b = input().split()
#     age.append([int(a), b])
#
# age.sort(key=lambda x: x[0])
# for i in age:
#     print(i[0], i[1])

# N = int(input())
# card_cnt = dict()
# temp = list(map(int, input().split()))
# for a in temp:
#     if a not in card_cnt:
#         card_cnt[a] = 0
#     card_cnt[a] += 1
#
# M = int(input())
# temp = list(map(int, input().split()))
# for a in temp:
#     if a in card_cnt:
#         print(card_cnt[a], end=' ')
#     else:
#         print("0", end=' ')

from collections import deque

N, K = map(int, input().split())

queue = deque()
for i in range(1, N+1):
    queue.append(i)

num = 1
print("<", end="")
while queue:
    if num == K:
        if len(queue) == 1:
            print(queue[0], end="")
        else:
            print(queue[0], end=", ")
        queue.popleft()
        num = 1
    else:
        queue.append(queue.popleft())
        num += 1
print(">")
