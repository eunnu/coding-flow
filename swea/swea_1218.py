for tc in range(1, 11):
    N = int(input())

    bk = input()

    stack = []
    flag = False

    for i in bk:
        if not stack:
            if i == '(' or i == '{' or i == '[' or i == '<':    # 괄호의 시작이 제대로 되는지 확인 하는 문
                stack.append(i)                                 # 시작이 여는 괄호면 넣어준다.
            else:
                flag = True                                     # 괄호의 시작을 닫는 괄호이면 제대로 된 괄호가 아니다.
                break                                           # 반복문 종료
        else:
            if i == ')':                                        # 소괄호 인 경우, i 가 닫는 소괄호 일때,
                if stack[-1] == '(':                            # 스택의 마지막 괄호가 여는 소괄호 라면
                    stack.pop()                                 # 빼준다
                else:                                           # 스택의 마지막 괄호가 소괄호가 아니라면, 넣어준다.
                    stack.append(i)

            elif i == '}':                                      # 중괄호 인 경우
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)

            elif i == ']':                                      # 대괄호 인 경우
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)

            elif i == '>':                                      # <> 인 경우
                if stack[-1] == '<':
                    stack.pop()
                else:
                    stack.append(i)
            else:                                               # 닫는 괄호가 아닌 여는 괄호 인데 스택이 비어 있지 않는 경우 넣어줌
                stack.append(i)

    if flag or stack:
        print(f"#{tc} {0}")
    else:
        print(f"#{tc} {1}")