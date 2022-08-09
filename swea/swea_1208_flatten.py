T = 10                                                      # 테스트 케이스 : 10

for tc in range(1, T + 1):                                  # 테스트케이스 1부터 10까지 반복

    N = int(input())                                        # 이동 횟수를 입력 받음
    box_li = list(map(int, input().split()))                # 박스의 높이를 입력 받음

    while N > 0:                                            # 이동 횟수 만큼 반복
        maxi_idx = 0                                        # 가장 높은 박스의 위치 값
        mini_idx = 0                                        # 가장 낮은 박스의 위치 값

        for i in range(100):                                # 100개 만큼 반복
            if box_li[i] > box_li[maxi_idx]:                # 만약 가장 높은 박스의 위치보다 현재 박스의 높이가 더 높다면
                maxi_idx = i                                # 인덱스 업데이트

            if box_li[i] < box_li[mini_idx]:                # 가장 낮은 박스의 위치보다 현재 박스의 높이가 더 낮다면
                mini_idx = i                                # 인덱스 업데이트

        if box_li[maxi_idx] - box_li[mini_idx] <= 1:        # 이동 횟수가 남았는데 가장 높은 박스와 낮은 박스의 차가 1 이하인 경우
            break                                           # 반복문 종료

        box_li[maxi_idx] -= 1                               # 가장 높은 위치의 박스 한개를
        box_li[mini_idx] += 1                               # 가장 낮은 위치로 옮겨줌

        N -= 1                                              # 이동 횟수를 1만큼 차감

    maxi_idx = 0                                            # 가장 높은 위치 변수
    mini_idx = 0                                            # 가장 낮은 위치 변수

    for i in range(100):                                    # 100만큼 반복
        if box_li[i] > box_li[maxi_idx]:                    # 만약 가장 높은 박스의 위치보다 현재 박스의 높이가 더 높다면
            maxi_idx = i                                    # 인덱스 업데이트

        if box_li[i] < box_li[mini_idx]:                    # 가장 낮은 박스의 위치보다 현재 박스의 높이가 더 낮다면
            mini_idx = i                                    # 인덱스 업데이트

    print(f"#{tc} {box_li[maxi_idx] - box_li[mini_idx]}")   # 결과 출력
