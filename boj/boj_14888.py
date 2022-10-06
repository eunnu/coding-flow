def sol(depth, number):
    global min_ans, max_ans
    if depth == N:
        if min_ans > number:
            min_ans = number
        if max_ans < number:
            max_ans = number
        return

    else:
        for idx in range(4):
            A = num[depth]
            if plus[idx]:
                if idx == 0:
                    plus[idx] -= 1
                    sol(depth+1, number + A)
                elif idx == 1:
                    plus[idx] -= 1
                    sol(depth+1, number - A)
                elif idx == 2:
                    plus[idx] -= 1
                    sol(depth+1, number * A)
                else:
                    plus[idx] -= 1
                    if number < 0 and (A > 0):
                        sol(depth+1, (number*(-1)//A)*(-1))
                    else:
                        sol(depth+1, number//A)
                plus[idx] += 1


N = int(input())

num = list(map(int, input().split()))
plus = list(map(int, input().split()))

min_ans = 999999999
max_ans = -999999999

sol(1, num[0])

print(max_ans)
print(min_ans)