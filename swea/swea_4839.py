T = int(input())                                                        # 테스트 케이스 수를 입력받음

for tc in range(1, T+1):                                                # 1부터 T까지 반복
    P, A, B = map(int, input().split())

    la, lb, ra, rb = 1, 1, P, P                                         # A, B의 왼쪽 오른쪽의 변수

    ans = ''                                                            # 답을 넣어줄 변수 선언
    while True:                                                         # 반복문 시작
        ac = int((la+ra)/2)                                             # A의 중간점 계산
        bc = int((lb+rb)/2)                                             # B의 중간점 계산

        if ac == A and bc == B:                                         # 둘 다 찾아야 하는 쪽을 찾았다면
            ans = '0'                                                   # 0
            break                                                       # 반복문 종료
        elif ac == A and bc != B:                                       # A만 찾았다면
            ans = 'A'                                                   # A
            break                                                       # 반복문 종료
        elif ac != A and bc == B:                                       # B만 찾았다면
            ans = 'B'                                                   # B
            break                                                       # 반복문 종료

        if A < ac:                                                      # 만약 A가 찾아야 하는 쪽이 중간 보다 작다면
            ra = ac                                                     # r을 바꿔 준다.
        if B < bc:                                                      # 만약 A가 찾아야 하는 쪽이 중간 보다 크다면
            rb = bc                                                     # l을 바꿔 준다.
        if A > ac:                                                      # 만약 B가 찾아야 하는 쪽이 중간 보다 작다면
            la = ac                                                     # r을 바꿔 준다.
        if B > bc:                                                      # 만약 B가 찾아야 하는 쪽이 중간 보다 크다면
            lb = bc                                                     # l을 바꿔 준다.

    print(f"#{tc} {ans}")                                               # 결과 출력
