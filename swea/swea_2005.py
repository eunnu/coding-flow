T = int(input())

for tc in range(1, T+1):
    N = int(input())

    p = [[1], [1, 1]]

    for i in range(2, N):
        p.append([1])
        for j in range(len(p[i-1])-1):
            p[i].append(p[i-1][j]+p[i-1][j+1])
        p[i].append(1)

    print(f"#{tc}")
    for i in range(N):
        for j in p[i]:
            print(j, end=" ")
        print()

