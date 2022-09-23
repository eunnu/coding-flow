# 시작시간을 기준으로 정렬, 시작시간이 같다면 도착 시간 기준으로 정렬
# 처음부터 돌면서 맨 앞에 있는 친구들만 확인해줌
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    li.sort(key=lambda x: (x[0], x[1]))
    ans = 0

    for i in range(N-1, -1, -1):
        start = li[i][0]
        j = N-1
        cnt = 1
        while j >= 0:
            if li[j][1] <= start:
                start = li[j][0]
                cnt += 1
                continue
            j -= 1

            if cnt > ans:
                ans = cnt

    print(f"#{tc} {ans}")