T = int(input())                                     # 테스트 케이스 갯수를 입력받음

for tc in range(1, T+1):                             # 테스트케이스 변수 tc 선언 후 1부터 T까지 반복

    N = int(input())                                 # 카드 장수를 입력 받음
    num = int(input())                               # 공백 없이 주어지는 카드 숫자를 num에 입력 받음

    card = []                                        # 카드 정보를 담아 줄 card list 선언
    cnt = 0                                          # 카드의 수와 N의 값을 비교해 줄 cnt 선언

    while cnt < N:                                   # cnt와 카드 장 수가 같아질때까지 반복
        cnt += 1                                     # 카운트 해줌
        card.append(num%10)                          # card 리스트에 num을 10으로 나눈 나머지를 넣어줌
        num = num // 10                              # num을 10으로 나누어 줌

    for i in range(N-1):                             # 0부터 N-1까지 반복
        for j in range(i+1, N):                      # i+1부터 N까지 반복
            if card[i] < card[j]:                    # 만약 card[i] 보다 card[j]가 작을 경우 -> 내림 차순 정렬
                card[i], card[j] = card[j], card[i]  # 두 개의 카드를 바꿔줌

    print(card)
    card_cnt = 0                                     # 반복 되는 숫자의 카드 수를 카운트 해줄 변수
    cnt_maxi = 0                                     # 카드 수의 크기를 비교 해 줄 변수
    card_info = 0                                    # 가장 많이 반복되는 수의 카드 번호를 넣어 줄 변수
    for i in range(1, N):                            # 1 부터 N 까지 반복
        if card[i-1] == card[i]:                     # 현재 카드와 전 카드의 숫자가 같은 경우
            card_cnt += 1                            # 카운트 + 1

        else:                                        # 같지 않다면
            if card_cnt > cnt_maxi:                  # 현재 카운트와 가장 많은 카운트를 비교
                cnt_maxi = card_cnt                  # 더 많은 카운트를 maxi에 넣어준다.
                card_info = card[i-1]                # 현재 카드와 이전 카드의 숫자가 다르기 때문에 이전 카드를 넣어 줌
            card_cnt = 0                             # 카운트를 초기화 해준다.

    print(f"#{tc} {card_info} {cnt_maxi}")           # 결과 출력
