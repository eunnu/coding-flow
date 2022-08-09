T = int(input())                                     # 테스트 케이스 갯수를 입력받음

for tc in range(1, T+1):                             # 테스트케이스 변수 tc 선언 후 1부터 T까지 반복
    N, M = input().split()                           # N과 M의 입력을 받음
    N = int(N)                                       # N을 정수화 시킴
    M = int(M)                                       # M을 정수화 시킴

    num = list(map(int, input().split()))            # 배열 정보를 입력 받음

    sum_min = 987654321                              # 합이 가장 작은 변수를 매우 큰 값으로 초기화
    sum_max = 0                                      # 합이 가장 큰 변수를 0으로 초기화

    for i in range(N-M+1):                           # 0부터 N - M 만큼 반복
        sum_num = 0                                  # 합 변수를 선언
        for j in range(i, i + M):                    # 현재 위치부터 M만큼 반복
            sum_num += num[j]                        # 각 배열의 값을 더해줌

        if sum_min > sum_num:                        # 만약 합이 가장 작은 합 보다 작다면
            sum_min = sum_num                        # 가장 작은 합을 업데이트
        if sum_max < sum_num:                        # 만약 합이 가장 큰 합 보다 크다면
            sum_max = sum_num                        # 가장 큰 합을 업데이트

    print(f"#{tc} {sum_max-sum_min}")                # 결과 출력


