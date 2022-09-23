# 하나의 세트가 3개 이상인 경우 부터 함수로 보내진다.
# 중복 제거용과 일반용으로 두개 씩 넣어줌
def game():
    # p1, p2 는 triple 용
    # p1_set, p2_set 은 run 용
    global ans, check
    for idx in range(len(p1) - 2):
        flag, cnt = False, 0
        for jdx in range(idx, idx+2):
            if p1[jdx] != p1[jdx+1]:
                flag = True
                break
        if not flag:
            ans, check = 1, True
            break
    for idx in range(len(p1_set) - 2):
        cnt = 1
        for jdx in range(idx, idx + 2):
            if p1_set[jdx] + 1 == p1_set[jdx+1]:
                cnt += 1
        if cnt == 3:
            ans, check = 1, True
            break

    if ans:
        return

    for idx in range(len(p2) - 2):
        flag, cnt = False, 0
        for jdx in range(idx, idx + 2):
            if p2[jdx] != p2[jdx + 1]:
                flag = True
                break

        if not flag:
            ans, check = 2, True
            break

    for idx in range(len(p2_set) - 2):
        cnt = 1
        for jdx in range(idx, idx + 2):
            if p2_set[jdx] + 1 == p2_set[jdx + 1]:
                cnt += 1

        if cnt == 3:
            ans, check = 2, True
            break


T = int(input())
for tc in range(1, T+1):
    li = list(map(int, input().split()))

    p1, p1_set, p2, p2_set = [], [], [], []
    ans, check = 0, False

    for i in range(len(li)):
        if i % 2:
            p2.append(li[i])
        else:
            p1.append(li[i])

        if i >= 4:
            p1.sort()
            p2.sort()
            p1_set = list(set(p1))
            p2_set = list(set(p2))
            game()
            if ans or check:
                break

    print(f"#{tc} {ans}")