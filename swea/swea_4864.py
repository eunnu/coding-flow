T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()

    ans = 0
    if N in M:
        ans = 1

    print(f"#{tc} {ans}")