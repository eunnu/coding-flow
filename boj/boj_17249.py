taebo = input()

right = 0
left = 0

flag = False
for i in taebo:
    if not flag and i == '@':
        left += 1

    elif i == ')':
        flag = True

    elif flag and i == '@':
        right += 1


print(left, right)