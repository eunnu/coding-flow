T = 10                                                                  # 테스트 케이스 수 : 10개

for _ in range(T):                                                      # 10 번 반복
    tc = int(input())                                                   # 테스트 케이스 번호를 매번 첫 줄에 주어짐

    arr = []                                                            # 배열 리스트를 선언
    for i in range(100):                                                # 100x100이므로 100 줄 반복
        arr.append(list(map(int, input().split())))                     # 한줄 씩 입력을 받음

    maxi = 0                                                            # 가장 큰 값을 넣어 줄 변수 선언
    for i in range(100):                                                # 세로 100 번
        sum_y, sum_x, sum_yx, sum_xy = 0, 0, 0, 0                       # 세로, 가로, 왼오대각, 오왼대각 더한 값 변수
        for j in range(100):                                            # 가로 100 번
            sum_y += arr[j][i]                                          # 세로 줄 더한 값
            sum_x += arr[i][j]                                          # 가로 줄 더한 값
            if i == j:                                                  # 대각선 더해 줄 조건 -> 왼오대각은 가로 세로 인덱스가 같음
                sum_yx = arr[i][j]                                      # 왼오대각 더해줌
                sum_xy = arr[i][99-i]                                   # 오왼 대각은 저러한 규칙을 갖고 있음

        if maxi < sum_x:                                                # 만약 맥스값보다 가로 합이 크다면
            maxi = sum_x                                                # max 업데이트
        if maxi < sum_y:                                                # 만약 맥스값보다 세로 합이 크다면
            maxi = sum_y                                                # max 업데이트
        if maxi < sum_yx:                                               # 만약 맥스값보다 왼오대각 합이 크다면
            maxi = sum_yx                                               # max 업데이트
        if maxi < sum_xy:                                               # 만약 맥스값보다 오왼대각 합이 크다면
            maxi = sum_xy                                               # max 업데이트

    print(f"#{tc} {maxi}")                                              # 결과 출력

