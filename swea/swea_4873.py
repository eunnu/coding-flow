T = int(input())

for tc in range(1, T+1):
    st = input()

    stack = []
    for i in st:
        if not stack:              # 스택이 비었으면 넣어주고
            stack.append(i)
        else:                      # 요소가 있는데
            if i == stack[-1]:     # 중복이야?
                stack.pop()        # 그럼 빼주고
            else:                  # 아니야?
                stack.append(i)    # 그럼 넣어주고

    ans = len(stack)
    print(f"#{tc} {ans}")