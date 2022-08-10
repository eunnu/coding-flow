T = int(input())                                            # 테스트 케이스 입력받음

for tc in range(1, T + 1):                                  # 테스트케이스 1부터 T까지 반복

    arr = list(map(int, input().split()))                   # 배열을 입력 받음

    ans = 0                                                 # 정답 변수 선언

    for i in range(1 << 10):                                # 부분 집합의 개수 만큼 반복
        check = False                                       # if 문을 통과했는지 확인해 줄 변수
        sum_arr = 0                                         # 각 조합의 합 변수
        for j in range(10):                                 # 10 만큼 반복
            if i & (1 << j):                                # i의 j번 비트가 1이라면
                sum_arr += arr[j]                           # j번 원소를 더해준다.
                check = True                                # 통과했으니까 check = True
        if check and sum_arr == 0:                          # 만약 if 문 통과하고 합이 0이라면
            ans = 1                                         # 부분집합의 합이 0이니까 ans = 1
            break                                           # 반복문 종료
    print(f"#{tc} {ans}")                                   # 결과 출력