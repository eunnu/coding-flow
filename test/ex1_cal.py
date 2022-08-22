T = int(input())

for tc in range(1, T+1):
    st = input()
    ex = ['+', '-', '*', '/']
    stack = []
    ans = ''

    for i in st:
        if i in ex:
            stack.append(i)
        else:
            ans += i

    while stack:
        ans += stack.pop()

    print(f"#{tc} {ans}")