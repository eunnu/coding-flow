# 재귀로 구현하는데 visit 에 방문한 흔적이 있다면 재 방문하지 않는다.
def v(num):
    global ans
    visit.add(num)
    ans += 1

    for idx in range(M):
        if computer[idx][0] == num:
            if computer[idx][1] not in visit:
                v(computer[idx][1])
        if computer[idx][1] == num:
            if computer[idx][0] not in visit:
                v(computer[idx][0])
    return


N = int(input())
M = int(input())
computer = [list(map(int, input().split())) for _ in range(M)]

ans = 0
visit = set()
visit.add(1)
for i in range(M):
    if computer[i][0] == 1:
        if computer[i][1] not in visit:
            v(computer[i][1])
    if computer[i][1] == 1:
        if computer[i][0] not in visit:
            v(computer[i][0])

print(ans)