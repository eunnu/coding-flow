T = int(input())
for tc in range(1, T+1):
    bk = input()

    stack = []

    for i in bk:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.append(i)
            else:
                stack.pop()

    if stack:
        print(f"{tc} {-1}")
    else:
        print(f"{tc} {1}")