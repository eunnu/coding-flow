# S = input()
# N = int(input())
# print(S[N-1])

# 가로 14
# 세로 6
# first = " " * 9 + ",r\'\"7"
# second = "r`-_   ,\'  ,/"
# third = " \\. \". L_r\'"
# forth = "   `~\\/"
# fifth = "      |"
# print(first)
# print(second)
# print(third)
# print(forth)
# print(fifth)
# print(fifth)
# N = int(input())
# num = list(map(int, input().split(" ")))
#
# num.sort()
# print(num[0], num[-1])

# max_num = 0
# max_loc = 10
# for i in range(9):
#     temp = int(input())
#     if max_num < temp:
#         max_num = temp
#         max_loc = i
#
# print(max_num)
# print(max_loc+1)

# S = input().split(" ")
# if S[0] == S[-1] == "":
#     print(len(S) - 2)
# elif S[0] == "" or S[-1] == "":
#     print(len(S) - 1)
# else:
#     print(len(S))

# S = input()
# S = S.upper()
# alpha_cnt = dict()
#
# for i in S:
#     if i in alpha_cnt:
#         alpha_cnt[i] += 1
#     else:
#         alpha_cnt[i] = 1
#
# result = sorted(alpha_cnt.items(), key=lambda x: x[1], reverse=True)
# if len(result) > 1 and result[0][1] == result[1][1]:
#     print("?")
# else:
#     print(result[0][0])

# KOI = list(map(int, input().split()))
# result = 0
# for i in KOI:
#     result += i*i
#
# print(result % 10)

# num = 1
# for _ in range(3):
#     num *= int(input())
#
# num_cnt = dict()
# for i in range(10):
#     num_cnt[i] = 0
#
# while num > 0:
#     num_cnt[num % 10] += 1
#     num //= 10
#
# for i in range(10):
#     print(num_cnt[i])

# a = "1 2 3 4 5 6 7 8"
# b = "8 7 6 5 4 3 2 1"
# r = input()
# if a == r:
#     print("ascending")
# elif b == r:
#     print("descending")
# else:
#     print("mixed")

# percent = set()
# for _ in range(10):
#     percent.add(int(input()) % 42)
#
# print(len(percent))


# T = int(input())
# quiz = [input() for _ in range(T)]
#
# for i in range(T):
#     score = 0
#     result = 0
#
#     for j in quiz[i]:
#         if j == "O":
#             score += 1
#             result += score
#         else:
#             score = 0
#     print(result)

T = int(input())
for _ in range(T):
    W, H, P = map(int, input().split(" "))
    if P % W == 0:
        result = str(W)

        if P//W < 10:
            result += "0" + str(P//W)
        else:
            result += str(P//W)
    else:
        result = str(P % W)

        if P//W < 9:
            result += "0" + str(P//W + 1)
        else:
            result += str(P//W + 1)

    print(result)