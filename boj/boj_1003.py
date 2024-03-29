# def fibonacci(num):
#     if num == 0:
#         result[0] += 1
#         return 0
#     elif num == 1:
#         result[1] += 1
#         return 1
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)
#
#
n = int(input())
for i in range(n):
    number = int(input())
    dp = [[1, 0], [0, 1]]
    for j in range(2, number+1):
        temp = [dp[j - 2][0] + dp[j-1][0], dp[j - 2][1] + dp[j-1][1]]
        dp.append(temp)

    print(dp[number][0], dp[number][1])