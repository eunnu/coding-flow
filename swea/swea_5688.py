# 범위를 좁혀가며 무식하게 풀예정

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    ans = -1

    for i in range(1, N//2):
        if i**3 == N:
            ans = i
            break

        elif i**3 > N:
            break

    print(f"#{tc} {ans}")