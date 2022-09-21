# 정점에서 왼쪽 -> 오른쪽으로 도는데
# 정점이 부호라면 자식 노드 부터 확인

def sol(idx):
    if len(tree[idx]) > 2:
        if tree[idx][1] in a:
            sol(int(tree[idx][2]) - 1)
            sol(int(tree[idx][3]) - 1)

            num2 = stack.pop()
            num1 = stack.pop()
            if tree[idx][1] == "+":
                stack.append(num1+num2)
            elif tree[idx][1] == "-":
                stack.append(num1-num2)
            elif tree[idx][1] == "*":
                stack.append(num1*num2)
            else:
                stack.append(num1//num2)
            return
    else:
        stack.append(int(tree[idx][1]))
        return

for tc in range(1, 11):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]

    a = ["+", "-", "*", "/"]
    stack = []
    ans = 0
    sol(0)

    print(f"#{tc} {stack[0]}")