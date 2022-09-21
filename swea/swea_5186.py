# 2를 곱해주었을 때,
# 1보다 크면 1
# 1보다 작으면 0
# 정수를 빼고 소수부분만 다시 곱해준다.
# 같은 소수부가 반복되거나, 소수부가 0이 되면 종료


T = int(input())
for tc in range(1, T+1):
    num = float(input())

    ans = ""
    depth = 0
    visited = set()
    visited.add(num)

    while True:
        num *= 2
        if num >= 1:
            ans += "1"
            num -= 1
        else:
            ans += "0"
        if num in visited:
            break
        if num == 0.0:
            break
        visited.add(num)
        depth += 1
        if depth > 12:
            ans = "overflow"
            break

    print(f"#{tc} {ans}")