T = int(input())

for tc in range(1, T+1):

    N = int(input())

    stu = []
    for _ in range(N):
        stu.append(list(map(int, input().split())))

    time = 1
    for i in range(N):
        for j in range(0, N):
            if i == j:
                continue
            if stu[j][0] <= stu[i][1] <= stu[j][1] or stu[j][0] <= stu[i][0] <= stu[j][1]:
                time += 1

    print(f"#{tc} {time}")