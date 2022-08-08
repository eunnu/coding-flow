T = 10                                              # 테스트 케이스 수 : 10개

for tc in range(1, T + 1):                          # 테스트 케이스 수 만큼 반복

    n = int(input())                                # 가로의 길이를 입력 받음
    building = list(map(int, input().split()))      # 그 길이만큼의 building 의 높이를 받음
    cnt = 0                                         # 세대수를 카운트 하기 위한 변수

    for i in range(2, len(building)-2):             # 처음과 끝 두개의 인덱스는 0이므로 그 사이를 범위 설정해줌

        left = 0                                    # 왼쪽 건물의 높이를 넣어줄 변수
        right = 0                                   # 오른쪽 건물의 높이를 넣어줄 변수
        now = building[i]                           # 현재 위치의 건물의 높이를 넣어줄 변수

        if building[i-1] <= building[i-2]:          # 만약 바로 옆 왼쪽 건물보다 옆옆 건물이 높거나 같으면
            left = building[i-2]                    # 왼쪽 건물의 높이는 옆옆 건물의 높이
        elif building[i-1] > building[i-2]:         # 바로 옆 왼쪽 건물이 옆옆 건물보다 높으면
            left = building[i-1]                    # 왼쪽 건물의 높이는 옆 건물의 높이

        if building[i+1] < building[i+2]:           # 만약 바로 옆 오른쪽 건물보다 옆옆 건물이 높거나 같으면
            right = building[i+2]                   # 오른쪽 건물의 높이는 옆옆 건물의 높이
        elif building[i+1] >= building[i+2]:        # 바로 옆 오른쪽 건물이 옆옆 건물보다 높으면
            right = building[i+1]                   # 오른쪽 건물의 높이는 옆 건물의 높이

        if left >= now or right >= now:             # 왼쪽 높이와 오른쪽 높이보다 현재 높이가 낮은 경우 continue
            continue

        if left > right:                            # 왼쪽보다 오른쪽이 더 크면
            cnt += now - left                       # 세대 수는 현재 건물 - 왼쪽 건물 높이
        else:                                       # 오른쪽 보다 왼쪽이 더 크면
            cnt += now - right                      # 세대 수는 현재 건물 - 오른쪽 건물 높이

    print(f"#{tc} {cnt}")                           # 정답 출력
