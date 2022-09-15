# 중위 순회이므로 중위 순회 함수를 돌려 스택에 해당 값들을 넣어주고 후에 연산한다.


def order(idx):
    if len(tree[idx]) == 2:
        stack.append(tree[idx][1])
        visited.add(idx+1)
        return

    else:
        for i in range(2, len(tree[idx])):
            if int(tree[idx][i]) not in visited:
                order(int(tree[idx][i])-1)

            if int(tree[idx][0]) not in visited:
                stack.append(tree[idx][1])
                visited.add(int(tree[idx][0]))
    return


for tc in range(1, 11):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]

    visited = set()
    stack = []

    order(0)
    arr = ['+', '-', '*', '/']

    while len(stack) != 1:
        a = stack.pop(0)
        b = stack.pop(0)
        c = stack.pop(0)
        a, c = int(a), int(c)
        maxi = max(a, c)
        mini = min(a, c)

        if b == '+':
            stack.append(str(a + c))
        elif b == '-':
            stack.append(str(maxi - mini))
        elif b == '/':
            stack.append(str(maxi // mini))
        else:
            stack.append(str(a * c))

        if len(stack) == 3 and stack[0] in arr:
            tmp = stack.pop()
            stack.insert(0, tmp)
        elif len(stack) == 3 and stack[1] in arr:
            pass
        elif len(stack) == 3 and stack[2] in arr:
            tmp = stack.pop(0)
            stack.append(tmp)

        if stack and (stack[0] in arr or stack[2] in arr):
            tmp = stack.pop(0)
            stack.append(tmp)

    print(f"#{tc} {stack[0]}")
