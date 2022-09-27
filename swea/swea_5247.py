T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = M - N
    stack = [[[N, 0]]]
    visited = dict()
    while stack != [[]]:
        arr = stack.pop()
        tmp = []
        flag = False
        while arr:
            [a, cnt] = arr.pop()
            if a == M:
                if ans > cnt:
                    ans = cnt
                break
            if a > M:
                if ans > a - M + cnt - 1:
                    ans = a - M + cnt - 1
                continue

            if ans < cnt:
                break

            if a < M:
                if ans > M - a + cnt:
                    ans = M - a + cnt
                    continue

            if a - 1 > 0 and ((a, a - 1) not in visited.keys() or visited[(a, a - 1)] > cnt):
                tmp.append([a - 1, cnt + 1])
                visited[(a, a - 1)] = cnt
            if (a, a + 1) not in visited.keys() or visited[(a, a + 1)] > cnt:
                tmp.append([a + 1, cnt + 1])
                visited[(a, a + 1)] = cnt
            if a - 10 > 0 and ((a, a - 10) not in visited.keys() or visited[(a, a - 10)] > cnt):
                tmp.append([a - 10, cnt + 1])
                visited[(a, a - 10)] = cnt

            tmp.append([a * 2, cnt + 1])

        stack.append(tmp)

    print(f"#{tc} {ans}")