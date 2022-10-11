# 인접한 칸에 좋아하는 친구가 가장 많은게 1
# 인접한 칸에 빈칸이 가장 많은게 2
# 가장 위 가장 왼쪽이 3

# 1-0. 모든 칸을 돌면서 친구의 개수를 센다. - check
# 1-1. 동시에 빈칸도 같이 센다. - check
# 1-2. 정렬한다.
# 2-0. 가장 앞의 자리에 넣어준다.
# 위의 과정을 N*N번 반복해준다.
def seat(num):
    for idx in range(N):
        for jdx in range(N):
            friend, cnt = 0, 0
            if cls[idx][jdx]:
                continue
            for d in range(4):
                ny = idx + dy[d]
                nx = jdx + dx[d]

                if 0 <= ny < N and 0 <= nx < N:
                    if cls[ny][nx] in li[num][1:5]:
                        friend += 1
                    elif not cls[ny][nx]:
                        cnt += 1

            cnt_li.append([friend, cnt, idx, jdx])


N = int(input())
li = [list(map(int, input().split())) for _ in range(N*N)]
cls = [[0] * N for _ in range(N)]

li_dic = dict()
for i in range(N*N):
    li_dic[li[i][0]] = li[i][1:5]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

for i in range(N*N):
    cnt_li = []
    seat(i)
    cnt_li.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    tmp = cnt_li[0]
    cls[tmp[2]][tmp[3]] = li[i][0]
print(cls)
ans = 0
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
for i in range(N):
    for j in range(N):
        c = 0
        for d in range(4):
            ni = i + dy[d]
            nj = j + dx[d]

            if 0 <= ni < N and 0 <= nj < N:
                if cls[ni][nj] in li_dic[cls[i][j]]:
                    c += 1
        ans += score[c]

print(ans)