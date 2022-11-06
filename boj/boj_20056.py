# 순서 대로 진행
# 방향으로 속도만큼 이동
# 1번과 N번은 이어져 있다.
# 한 좌표에 여러 개가 존재하면 질량/5,속력/개수,
# 방향은 모두 홀수, 짝수이면 0,2,4,6 아니면 1,3,5,7
def sol(index, number):                         # 파이어볼 나누는 구역
    flag = False
    hol_jack = 0
    if ball[number[0]][4] % 2:
        hol_jack = 1
    sum_m = ball[number[0]][2]
    sum_s = ball[number[0]][3]
    ball[number[0]][2] = 0
    for num in range(1, len(number)):
        sum_m += ball[number[num]][2]
        sum_s += ball[number[num]][3]
        if ball[number[num]][4] % 2 != hol_jack:        # 홀짝 확인해서
            flag = True
        ball[number[num]][2] = 0

    di = [[0, 2, 4, 6], [1, 3, 5, 7]]                   # 파이어볼 노나줌
    cnt = len(number)
    for dire in range(4):
        ball.append([index[0], index[1], sum_m//5, sum_s//cnt, di[flag][dire]])


def move_ball():                                        # 파이어볼 이동중
    fire_ball = dict()

    for idx in range(len(ball)):
        by, bx, d = ball[idx][0], ball[idx][1], ball[idx][4]
        if ball[idx][2] == 0:
            continue
        for j in range(ball[idx][3]):
            by += dy[d]
            bx += dx[d]
            if by < 1:
                by = N
            if by > N:
                by = 1
            if bx < 1:
                bx = N
            if bx > N:
                bx = 1
        if (by, bx) not in fire_ball:
            fire_ball[(by, bx)] = []
        fire_ball[(by, bx)].append(idx)                 # 일단 모일지 모르니 딕셔너리에 좌표값으로 넣어주고
        ball[idx][0], ball[idx][1] = by, bx             # 이동된 위치값 업데이트

    for check in fire_ball.keys():
        if len(fire_ball[check]) > 1:                   # 모여있는 파이어볼이 있다면 노나주러 감
            sol(check, fire_ball[check])


N, M, K = map(int, input().split())
ball = [list(map(int, input().split())) for _ in range(M)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    move_ball()

ans = 0
for i in range(len(ball)):
    ans += ball[i][2]

print(ans)
