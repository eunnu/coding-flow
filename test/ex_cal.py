T = 3
for tc in range(1, T + 1):
    st = input()
    stack = []
    fx = ''

    for i in st:
        if i == '(':
            stack.append(i)
        elif i == '+' or i == '-':
            if not stack:
                stack.append(i)
            elif stack:
                if stack[-1] == '(':
                    stack.append(i)
                else:
                    flag = True
                    while flag:
                        if not stack or (stack and stack[-1] == '('):
                            flag = False
                        else:
                            fx += stack.pop()
                    stack.append(i)
        elif i == '*' or i == '/':
            if not stack or stack and (stack[-1] == '(' or stack[-1] == '+' or stack[-1] == '-'):
                stack.append(i)
            else:
                flag = True
                while flag:
                    if stack and (stack[-1] == '(' or stack[-1] == '+' or stack[-1] == '-'):
                        flag = False
                    else:
                        fx += stack.pop()
                stack.append(i)

        elif i == ')':
            flag = True
            while flag:
                if stack and stack[-1] != '(':
                    fx += stack.pop()
                else:
                    flag = False

            stack.pop()
        else:
            fx += i

    while stack:
        a = stack.pop()
        if a != '(':
            fx += a

    print(f"#{tc} {fx}")