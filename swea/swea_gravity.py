#  솔루션 코드를 작성합니다.
T = int(input())                                # 테스트케이스 수 입력 받음

for tc in range(1, T+1):                        # 테스트케이스 변수 tc를 1부터 T까지 반복

    N = int(input())                            # 길이 N을 입력받음

    box = list(map(int, input().split(' ')))
    maxi = 0                                    # 얼마나 떨어졌는지를 넣어주기 위한 변수
    for i in range(N):                          # 길이 만큼 반복문을 돌려줌
        height = N - i - 1                      # 회전 시 바닥까지의 거리 변수 
        cnt = 0                                 # 현재 박스의 높이 보다 크거나 같은 박스를 카운트해주기 위한 변수
        for j in range(i+1, N):                 # 현재 박스 다음 박스 부터 마지막 박스까지 반복
            if box[i] <= box[j]:                # 만약 현재 박스보다 높이가 같거나 높다면
                cnt += 1                        # 카운트
        drop = height - cnt                     # drop변수에 회전 시 바닥까지의 거리에서 카운트 값을 빼준다.                      
        if maxi < drop:                         # 만일 중간값이 max값보다 크다면
            maxi = drop                         # maxi에 drop 값을 넣어준다.

    print(f"#{tc} {maxi}")                      # 결과 출력
