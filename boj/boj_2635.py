'''
일단 0.6을 곱해준 뒤에 그 수에서 +- 1을 해가면서 길이가 작아질 때 까지 비교 해줌
'''
N = int(input())

num1 = int(N*0.6)
num2 = num1
ans = [-1]
flag = True

while flag:
    number = num1
    tmp = [N, number]
    num3 = N
    num4 = number
    while number >= 0:
        number = num3 - num4
        if number >= 0:
            tmp.append(number)
        num3 = num4
        num4 = number

    if len(ans) <= len(tmp):
        ans.clear()
        for i in tmp:
            ans.append(i)
    else:
        flag = False

    num1 += 1

flag = True
while flag:
    number = num2
    tmp = [N, number]
    num3 = N
    num4 = number
    while number >= 0:
        number = num3 - num4
        if number >= 0:
            tmp.append(number)
        num3 = num4
        num4 = number

    if len(ans) <= len(tmp):
        ans.clear()
        for i in tmp:
            ans.append(i)
    else:
        flag = False
    num2 -= 1
print(len(ans))
print(*ans)