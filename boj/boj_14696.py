
N = int(input())

for _ in range(N):
    A = list(map(int, input().split()[1:]))
    B = list(map(int, input().split()[1:]))

    A.sort(reverse=True)                              # 내림 차순 정렬
    B.sort(reverse=True)                              # 내림 차순 정렬

    max_len = 0

    if len(A) < len(B):                               # 만약 B 의 길이가 더 길다면
        max_len = len(B)                              # 긴 길이는 B 의 길이이고
        for _ in range(len(B)-len(A)):                # A 는 뒤에 모자란 길이만큼 채워준다.
            A.append(0)
    else:                                             # 만약 A 의 길이가 더 길다면
        max_len = len(A)                              # 긴 길이는 A 의 길이이고
        for _ in range(len(A)-len(B)):                # B 는 뒤에 모자란 길이만큼 채워준다.
            B.append(0)

    flag = False                                      # 무승부인지 확인해 줄 변수
    for i in range(max_len):                          # 최대 길이만큼 반복
        if A[i] > B[i]:                               # 만약 A 카드가 더 크다면
            print('A')                                # A 출력
            flag = False                              # 승자가 정해졌다
            break                                     # 반복문 종료
        elif A[i] < B[i]:                             # 만약 B 카드가 더 크다면
            print('B')                                # A 출력
            flag = False                              # 승자가 정해졌다
            break                                     # 반복문 종료
        else:                                         # 비겼다
            flag = True                               # 일단 플래그를 건드리고
            continue                                  # 끝까지 가본다

    if flag:                                          # 플래그가 켜졌다?
        print('D')                                    # 무승부
