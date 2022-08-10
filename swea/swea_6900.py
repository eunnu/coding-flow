T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lotto = []
    for i in range(N):
        lotto.append(list(map(str, input().split(' '))))

    cnt_lotto = []

    for i in range(N):                                  # 카운팅 소트를 응용
        cnt_lotto.append([0] * 11)                      # 당첨 번호 갯수를 담아줄 리스트 선언
        for j in lotto[i][0]:                           # lotto[i][0] 번호 lotto[i][1] 금액
            if j == '*':                                # 만약 * 이면 마지막에 카운트
                cnt_lotto[i][10] += 1
            else:
                cnt_lotto[i][int(j)] += 1               # 만약 숫자라면 그 위치에 카운트

    money = 0                                           # 당첨금 변수
    for _ in range(M):                                  # M 만큼 반복

        lotto_num = int(input())                        # 로또 번호를 받아 줌
        num = []                                        # 그 번호를 받을 리스트 선언

        cnt = 0                                         # 8개 번호
        while cnt < 8:
            num.append(lotto_num % 10)                  # 10으로 나눈 나머지 값 넣어줌
            lotto_num = lotto_num // 10                 # 10으로 나누어 줌
            cnt += 1                                    # 카운트 해줌

        for i in range(N):                              # 로또 갯수 만큼 반복
            cnt_num = 8                                 # *이 필요한 갯수를 확인

            for j in range(8):
                if cnt_lotto[i][num[j]]:                # 만약 번호가 해당 복권의 당첨 번호라면
                    cnt_num -= 1                        # 갯수를 줄여줌

            if cnt_num == cnt_lotto[i][10]:            # 만약 남은 갯수와 *의 갯수가 같다면
                money += int(lotto[i][1])              # 당첨
                lotto[i][1] = '0'                      # 재 당첨은 없기 때문에 0으로 바꿔줌
    print(f"#{tc} {money}")
