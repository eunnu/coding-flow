# import sys
#
# N, M = map(int, sys.stdin.readline().split(" "))
# card = list(map(int, sys.stdin.readline().split(" ")))
#
# res = 0
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             if M - res > M - (card[i] + card[j] + card[k]) > -1:
#                 res = card[i] + card[j] + card[k]
#
# print(res)

