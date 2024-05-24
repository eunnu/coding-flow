import sys


# 시간초과 코드
N, r, c = map(int, sys.stdin.readline().split(" "))
res = -1


# def solution(y, x, num, nn, cnt):
#     global res
#     if num == 2:
#         for i in range(y, y + num):
#             for j in range(x, x + num):
#                 if i == r and j == c:
#                     res = cnt
#                     return
#                 cnt += 1
#         return
#     else:
#         next_num = num // 2
#         solution(y, x, next_num, nn - 1, cnt)  # 1 사분면
#         solution(y, x + next_num, next_num, nn - 1, cnt + 2**(nn-2)*2**nn)  # 2 사분면
#         solution(y + next_num, x, next_num, nn - 1, cnt + 2*2**(nn-2)*(2**nn))  # 3 사분면
#         solution(y + next_num, x + next_num, next_num, nn - 1, cnt + 3*2**(nn-2)*(2**nn))  # 4사분면
#         return
#
#
# solution(0, 0, 2**N, N, 0)

# 조건에 맞는 사분면만 재귀 할 수 있도록 해야 함.
# 1 사분면 : 2**(n-2) <= y < 2**(n-1) and 2**(n-2) <= x < 2**(n-1) => cnt +=
# 2 사분면 : 2**(n-2) <= y < 2**(n-1) and 2**(n-1) <= x < 2**n => cnt += 2**(2*n-2) - 1
# 3 사분면 : 2**(n-1) <= y < 2**n and 2**(n-2) <= x < 2**(n-1) => cnt += 2**(2*n-1) - 1
# 4 사분면 : 2**(n-1) <= y < 2**n and 2**(n-1) <= x < 2**n => cnt += 2**(2*n-2) + 2**(2*n-1) - 1


def solution(y, x, num):
    global res
    next_num = 2**(num - 1)
    if y == r and x == c:
        res += 1
        return

    if num == 1:
        if y <= r < y + 1:
            if x <= c < x + 1:
                res += 1
            elif x <= c < x + 2:
                res += 2
            return
        elif y + 1 <= r < y + 2:
            if x <= c < x + 1:
                res += 3
            elif x <= c < x + 2:
                res += 4
            return
    else:
        if y <= r < y + 2**(num-1):
            if x <= c < x + 2**(num-1):
                solution(y, x, num - 1)

            elif x + 2**(num-1) <= c < x + 2**num:
                res += 2 ** (2 * num - 2)
                solution(y, x + next_num, num - 1)
            return

        elif y + 2**(num-1) <= r < y + 2**num:
            if x <= c < x + 2**(num-1):
                res += 2**(2*num-1)
                solution(y + next_num, x, num - 1)

            elif x + 2**(num-1) <= c < x + 2**num:
                res += 2**(2*num-2) + 2**(2*num-1)
                solution(y + next_num, x + next_num, num - 1)
            return


solution(0, 0, N)
print(res)