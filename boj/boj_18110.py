import sys

N = int(sys.stdin.readline())
res = 0


def roundup(num1, num2):
    if num1/num2 - num1//num2 >= 0.5:
        return (num1 // num2) + 1
    else:
        return num1 // num2


if N > 0:
    cnt = 0
    score = list(int(sys.stdin.readline()) for _ in range(N))

    loss_n = roundup(15*N, 100)

    score.sort()

    for i in range(loss_n, N - loss_n):
        cnt += score[i]
    res = roundup(cnt, N-loss_n*2)

print(res)
