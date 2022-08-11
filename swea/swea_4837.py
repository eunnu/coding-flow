T = int(input())                                                        # 테스트 케이스 수를 입력받음

for tc in range(1, T+1):                                                # 1부터 T까지 반복
    N, K = map(int, input().split())                                    # N, P 입력받음

    arr = [i for i in range(1, 13)]                                     # 1 부터 12 를 넣은 배열을 선언

    cnt = 0                                                             # 개수를 세줄 변수
    for i in range(1 << 12):                                            # 모든 경우의 수를 돌면서
        mid_jip = []                                                    # 임시로 담아줄 리스트 선언
        for j in range(len(arr)):                                       # 배열 크기 만큼 돌면서
            if i & (1 << j):                                            # 조건을 만족하면
                mid_jip.append(arr[j])                                  # 리스트에 넣어준다.

        if len(mid_jip) == N and sum(mid_jip) == K:                     # 만약 길이가 N 이면서 합이 K이면
            cnt += 1                                                    # 카운트

    print(f"#{tc} {cnt}")                                               # 결과 출력