# T = int(input())                                    # 테스트 케이스 갯수를 입력받음
#
# for tc in range(1, T+1):                            # 테스트케이스 변수 tc 선언 후 1부터 T까지 반복
#
#     N = int(input())                                # 숫자의 개수를 담을 변수 선언
#     num = list(map(int, input().split(' ')))        # 숫자의 정보를 담을 num 리스트에 map을 사용하여 입력을 받음
#
#     mini, maxi = 98765432, 0                        # 최소값, 최대값을 넣을 mini, maxi 변수 선언
#                                                     # mini 는 입력 값의 범위 보다 큰 값을 넣어준다.
#     for i in range(N):                              # 0부터 N까지 반복
#         if maxi < num[i]:                           # 만약 현재 숫자가 maxi보다 큰 경우
#             maxi = num[i]                           # maxi에 현재 숫자를 넣어줌
#         elif mini > num[i]:                         # 만약 현재 숫자가 mini보다 작은 경우
#             mini = num[i]                           # mini에 현재 숫자를 넣어줌
#
#     print(f"#{tc} {maxi - mini}")                   # 결과 출력


T = int(input())                                    # 테스트 케이스 갯수를 입력받음

for tc in range(1, T+1):                            # 테스트케이스 변수 tc 선언 후 1부터 T까지 반복

    N = int(input())                                # 숫자의 개수를 담을 변수 선언
    num = list(map(int, input().split(' ')))        # 숫자의 정보를 담을 num 리스트에 map을 사용하여 입력을 받음

    for i in range(N-1):                            # 정렬하기 위해 0 부터 N-1 까지
        for j in range(i+1, N):                     # 현재 위치부터 N까지
            if num[i] > num[j]:                     # 처음 위치 값과 현재 위치 값을 비교해서
                num[i], num[j] = num[j], num[i]     # 자리를 바꿔줌

    print(f"#{tc} {num[-1] - num[0]}")              # 결과 출력