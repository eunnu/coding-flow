'''
밭의 세로의 중앙 열을 돌면서 중앙 까지 위 아래를 하나씩 늘려가며 더해주고
중앙을 지나는 시점 부터 위 아래를 하나씩 줄여가며 더해준다.
ex)
    0 1 2 3 4
    1 2 3 4 5
    2 3 4 5 6    <- 여기를 돌아 주는데
    3 4 5 6 7
    4 5 6 7 8

처음에는 2만 더해주고
3에서는 3하고 위 아래 2, 4를 더해주고
4에서는 4의 두 칸 위 아래, 한 칸 위 아래인 2, 6/ 3, 5 와 4를 더해준다.
5에서는 다시 위 아래 4, 6을 더해주고
6에서는 6만 더해준다.

순서대로 1, 3, 5, 3, 1 개 만큼 더해주는 것

'''


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = []
    for _ in range(N):
        area.append(list(map(int, list(input()))))

    mid = N//2
    ans = 0
    for i in range(N):
        ans += area[mid][i]
        if i <= mid:
            for j in range(1, i+1):
                ans += area[j + mid][i] + area[mid - j][i]
        else:
            for j in range(1, N-i):
                ans += area[j + mid][i] + area[mid - j][i]


    print(f"#{tc} {ans}")