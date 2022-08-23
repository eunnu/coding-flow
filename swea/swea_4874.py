T = int(input())

for tc in range(1, T+1):
    st = input().split()

    stack = []
    print(f"#{tc}", end=" ")
    for i in st:
        if len(stack) >= 2:
            if i == '+':
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(x1 + x2)
            elif i == '-':
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(x1 - x2)
            elif i == '*':
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(x1 * x2)
            elif i == '/':
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(x1 // x2)
            elif i == '.':
                print('error')
            else:
                stack.append(int(i))

        else:
            if i == '+' or i == '-' or i == '*' or i == '/':
                print('error')
                break
            elif i == '.' and stack:
                print(stack[-1])
            elif i == '.' and (not stack):
                print('error')
            else:
                stack.append(int(i))
