for tc in range(1, 11):
    N = int(input())

    st = input()

    stack = []                                                  # 연산자를 넣어 줄 스택
    fx = []                                                     # 후위식을 넣어 줄 리스트

    for i in st:
        if i == '(':                                            # 여는 괄호는 걍 넣어줌
            stack.append(i)

        elif i == '+':                                          # 더하기 연산자면
            if stack:
                if stack[-1] == '(':                            # 스택에 여는 괄호만 존재하면 넣고
                    stack.append(i)
                else:                                           # 아니면 여는 괄호만 남거나 다 빌 때까지 pop 해서 후위식에 다 넣은 후 스택에 넣어줌
                    flag = True
                    while flag:
                        if stack:
                            if stack[-1] == '(':
                                flag = False
                            else:
                                fx.append(stack.pop())
                        else:
                            flag = False
                    stack.append(i)
            else:                                               # 스택이 비어있으면 그냥 넣어줌
                stack.append(i)

        elif i == '*':                                          # 곱하기 연산자라면
            if stack:
                if stack[-1] == '+' or stack[-1] == '(':        # 스택에 여는 괄호와 더하기 연산자가 존재할 때는 걍 넣어주고
                    stack.append(i)
                else:                                           # 곱하기 연산자가 있으면 더하기 연산자나 여는 괄호를 만날 때까지 계속
                    flag = True                                 # pop 해서 후위식에 넣어주고 난 후 stack 에 넣어줌
                    while flag:
                        if stack:
                            if stack[-1] == '+' or stack[-1] == '(':
                                flag = False
                            else:
                                fx.append(stack.pop())
                        elif not stack:
                            flag = False
                    stack.append(i)
            else:                                               # 스택이 비어있으면 넣어주고
                stack.append(i)

        elif i == ')':                                          # 닫는 괄호는 여는 괄호를 만날 때까지 계속 pop 해서 식에 넣어주고
            flag = True                                         # 여는 괄호를 만나면 여는 괄호 빼서 버림
            while flag:
                if stack[-1] == '(':
                    stack.pop()
                    flag = False
                else:
                    fx.append(stack.pop())

        else:                                                   # 숫자는 int 로 변환하여 식에 넣어줌
            fx.append(int(i))

    while stack:                                                # 스택이 비어 있지 않다면
        if stack[-1] == '(':                                    # 여는 괄호라면 그냥 버리고
            stack.pop()
        else:                                                   # 아니면 식에 넣어줌
            fx.append(stack.pop())

    for i in range(len(fx)):                                    # 이제 그 식을 계산 할 차례
        if fx[i] == '+':                                        # 더하기야?
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(x1+x2)                                 # 앞에 두 개 빼서 더해서 다시 넣어

        elif fx[i] == '*':                                      # 곱하기야?
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(x1 * x2)                               # 앞에 두 개 빼서 곱해서 다시 넣어

        else:                                                   # 숫자야?
            stack.append(fx[i])                                 # 그냥 넣어

    print(f"#{tc} {stack[0]}")                                  # 계산 끝? 그럼 하나 남은거 출력