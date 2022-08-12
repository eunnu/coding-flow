T = 10                                                              # 테스트 케이스 수 : 10

for _ in range(1, T+1):                                             # 1부터 T까지 반복
    tc = int(input())                                               # 테스트 케이스 번호 입력 받음
    search_str = input()                                            # 찾아야 하는 단어를 입력 받음
    sent = input()                                                  # 문장을 입력 받음

    ans = 0                                                         # 정답 변수 선언

    cnt = 0                                                         # 연속되는 알파벳의 개수를 확인해 줄 변수
    for i in range(len(sent)):                                      # 문장의 길이만큼 반복
        for j in range(len(search_str)):                            # 찾아야 하는 단어의 길이 만큼
            if (i+j) < len(sent) and search_str[j] == sent[i+j]:    # 만약 그 두 개의 문자가 같다면
                cnt += 1                                            # 카운트
                if cnt == len(search_str):                          # 카운트의 개수가 찾아야 하는 단어의 길이와 같다면
                    ans += 1                                        # 찾은 개수 1개 카운트
                    cnt = 0                                         # 지금 위치를 반환
                    i = i + j
            else:                                                   # 연속 되지 않는다면
                cnt = 0                                             # 카운트 초기화

    print(f"#{tc} {ans}")                                           # 결과 출력