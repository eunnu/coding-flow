#  솔루션 코드를 작성합니다.
T = int(input())

for tc in range(1, T+1):
    bk = input()

    stack = []
    flag = True                                                 # 시작이 (, { 인지 확인해주는 변수

    for i in bk:
        if not stack:                                           # 스택이 비어있다면
            if i == '(' or i == '{':                            # 여는 괄호라면
                stack.append(i)                                 # 스택에 넣어주고
            elif i == ')' or i == '}':                          # 닫는 괄호라면
                flag = False                                    # 제대로 된 괄호가 아니므로
                break                                           # 반복문 종료

        else:                                                   # 스택에 요소가 있다면
            if i == '(' or i == ')' or i == '{' or i == '}':    # 문자가 괄호 요소인데
                if stack[-1] == '(' and i == ')':               # 스택 마지막이 여는 소괄호 인데 문자가 닫는 소괄호라면
                    stack.pop()                                 # 여는 소괄호 빼주고
                    continue

                if stack[-1] == '{' and i == '}':               # 스택 마지막이 여는 중괄호 인데 문자가 닫는 중괄호라면
                    stack.pop()                                 # 여는 중괄호 빼주고

                else:                                           # 또 여는 거면
                    stack.append(i)                             # 그냥 넣어주고

    if stack or not flag:                                       # 스택이 남아 있거나 시작이 잘못된 괄호라면
        print(f"#{tc} {0}")                                     # 0 출력
    else:
        print(f"#{tc} {1}")


