T = int(input())

for tc in range(1, T+1):
    kyu = list(map(int, input().split()))
    young = []
    for i in range(1, 19):
        if i in kyu:
            continue
        else:
            young.append(i)

    perm_y = []

    def perm(idx):                                              # 함수 구현
        if idx == 9:                                            # 인덱스 값이 9이면
            perm_y.append(list(k for k in young))               # 현재 인영이의 배열을 순열 리스트에 깊은 복사한다.
        else:                                                   # 인덱스 값이 0 ~ 8이라면
            for i in range(idx, 9):                             # 현재 위치에서 8까지
                young[idx], young[i] = young[i], young[idx]     # 현재 위치와 전달 받은 인덱스 위치의 값을 바꿔준다.
                perm(idx + 1)                                   # 인덱스를 올려 재귀
                young[idx], young[i] = young[i], young[idx]     # 원래 함수로 돌려 놔 준다.

    perm(0)

    win_cnt = 0
    lose_cnt = 0

    for i in range(len(perm_y)):
        score_y, score_k = 0, 0
        for j in range(9):
            if perm_y[i][j] > kyu[j]:
                score_y += perm_y[i][j] + kyu[j]
            else:
                score_k += perm_y[i][j] + kyu[j]

        if score_k == score_y:
            continue
        elif score_y > score_k:
            win_cnt += 1
        else:
            lose_cnt += 1

    print(f"#{tc} {lose_cnt} {win_cnt}")



