T = 10
for tc in range(1, T+1):
    N = int(input())
    stack = []
    fx = []
    st = input()

    for i in range(N):
        if st[i] == '+':
            if stack:
                while stack:
                    fx.append(stack.pop())
            stack.append(st[i])
        elif st[i] == '*':
            if stack and stack[-1] == '*':
                fx.append(stack.pop())
            stack.append(st[i])

        else:
            fx.append(int(st[i]))

    while stack:
        fx.append(stack.pop())

    for i in fx:
        if i != '*' and i != '+':
            stack.append(i)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)

    print(f"#{tc} {stack[0]}")