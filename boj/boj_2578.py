'''
빙고가 완성 되려면 적어도 13번은 번호가 불려 져야 한다.
안전하게 처음 10개를 먼저 지우고 확인하는 과정을 시작한다.
'''


def check():
    res = 0
    bs, rbs = 0, 0                          # 대각선, 역 대각선 확인 변수
    for idx in range(5):
        bx, by = 0, 0                       # 가로, 세로 확인 변수
        for jdx in range(5):
            bx += visited[idx][jdx]
            by += visited[jdx][idx]
            if idx == jdx:                  # 대각선, 역 대각선 확인 해줄 조건 문
                bs += visited[idx][jdx]
                rbs += visited[idx][4-jdx]
        if bx == 5:
            res += 1
        if by == 5:
            res += 1
    if bs == 5:
        res += 1
    if rbs == 5:
        res += 1
    return res


bingo = []
for i in range(5):
    bingo.append(list(map(int, input().split())))

number = []
for i in range(5):
    number.append(list(map(int, input().split())))

visited = [[0]*5 for _ in range(5)]
ana_i, ana_j, cnt = 0, 0, 0                             # 아나운서가 불러줄 번호 위치 인덱스
ans = 0
flag = True
while flag:
    for i in range(5):
        for j in range(5):
            if number[ana_i][ana_j] == bingo[i][j]:
                visited[i][j] = 1
                cnt += 1
                if cnt > 10:
                    ans = check()                       # 10 개 이상의 번호가 불렸을 때 부터 빙고인지 확인 해줌
                    if ans >= 3:                        # 3줄 이상일 경우 정답은 카운트 수 반복문 종료
                        ans = cnt
                        flag = False
                        break
                ana_j += 1
                if ana_j == 5:
                    ana_i += 1
                    ana_j = 0

print(ans)