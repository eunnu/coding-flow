T = int(input())                                                                        # 테스트케이스 수를 입력받음

for tc in range(1, T + 1):                                                              # 테스트 케이스 변수 tc를 1부터 T까지 반복    
    
    num = int(input())                                                                  # 연속되는 6자리 수를 입력받음
    card = []                                                                           # num을 넣어 줄 리스트 선언
    babygin = 0                                                                         # 베이비 진인지 확인해 줄 변수
    cnt = 0                                                                             # 리스트의 길이를 확인해 줄 변수 count

    while cnt <= 5:                                                                     # cnt를 뒤에서 +1 해주기 때문에 5까지 반복
        card.append(num%10)                                                             # card 리스트에 num을 10으로 나눈 나머지값을 넣어줌
        num = num//10                                                                   # num을 10으로 나누어줌
        cnt += 1                                                                        # 카운트 +1 해줌
        
    # 이 부분 부터 정렬
    for i in range(5):                                                                  # 0부터 4까지 반복
        for j in range(i+1, 6):                                                         # i+1부터 5까지 반복
            if card[i] > card[j]:                                                       # 만약 앞의 카드보다 뒤의 카드 수가 크면
                card[i], card[j] = card[j], card[i]                                     # 두 개의 카드의 위치를 바꾸어 줌
    
    # 1번 2번 케이스
    if (card[0] == card[1] == card[2]):                                                 # 첫 번째 경우 : 앞의 3장이 run인 경우
        if card[3] == card[4] == card[5]: babygin = 1                                   #               뒤의 3장이 run인 경우
        else:                                                                           # 두 번째 경우 : 앞의 3장이 run인 경우
            if (card[3] + 1) == card[4] and (card[4] + 1) == card[5]:                   #               뒤의 3장이 triplet인 경우
                babygin = 1                                                             # babygin 임

    # 3번 4번 케이스
    elif card[1] == (card[0] + 1) and card[2] == (card[1] + 1):                         # 세 번째 경우 : 앞의 3장이 triplet
        if card[3] == card[4] == card[5]: babygin = 1                                   #               뒤의 3장이 run
        else:                                                                           # 네 번째 경우 : 앞의 3장이 triplet
            if (card[3] + 1) == card[4] and (card[4] + 1) == card[5]:                   #               뒤의 3장이 triplet
                babygin = 1                                                             # babygin 임

    # 5번 케이스
    elif card[2] == (card[0] + 1) and card[4] == (card[2] + 1):                         # 다섯 번째 경우 : 예로 들어 112233 인 경우
        if  card[3] == (card[1] + 1) and card[5] == (card[3] + 1): babygin = 1          # babygin 임
            

    print(f"#{tc} {babygin}")                                                           # 결과 출력

    # 이러한 경우를 벗어나면서 babygin 인 경우 틀릴 수 있음
    # 혹시 그런 경우를 아시는 분 있으시면 연락줘요 추가할게요..