T = int(input())                                                        # 테스트 케이스 수를 입력받음

for tc in range(1, T+1):                                                # 1부터 T까지 반복
    N = int(input())                                                    # 구역의 수를 입력 받음

    color = []                                                          # 전체 구역의 리스트
    color_r = []                                                        # 빨간 색 구역만 넣어줄 리스트
    color_b = []                                                        # 파란 색 구역만 넣어줄 리스트

    for i in range(N):                                                  # 구역의 수만큼 반복
        color.append(list(map(int, input().split())))                   # 전체 구역을 입력 받음

        if color[i][-1] == 1:                                           # 색의 번호가 1이라면
            color_r.append(color[i][:-1])                               # 빨간 색 구역의 좌표만 넣어줌
        else:                                                           # 색의 번호가 2이라면
            color_b.append(color[i][:-1])                               # 파란 색 구역의 좌표만 넣어줌

    cnt = 0                                                             # 보라 색 구역의 수

    if color_b[0] == ([]) or color_r == ([]):                           # 만약 빨간 색, 파란 색 구역이 비어있다면
        print(f"#{tc} {cnt}")                                           # 겹치는 부분 없음
    else:                                                               # 둘다 구역이 존재한다면
        for i in range(len(color_r)):                                   # 빨간 구역 반복
            for j in range(len(color_b)):                               # 파란 구역 반복
                x, y = color_r[i][1], color_r[i][0]                     # 빨간색 시작 좌표 (y, x)
                while True:                                             # 빨간 구역 반복
                    if x > color_r[i][3] or y > color_r[i][2]:          # 구역을 벗어나면
                        continue                                        # 지나가

                    if color_b[j][0] <= y <= color_b[j][2] and color_b[j][1] <= x <= color_b[j][3]:
                        cnt += 1                                        # 그 좌표값이 파란색 구역 안에 있다면 보라색 카운트 +1

                    x += 1                                              # x 좌표 + 1
                    if x > color_r[i][3]:                               # 만약 x가 구역을 벗어나면
                        y += 1                                          # y 좌표 + 1
                        x = color_r[i][1]                               # x 좌표는 원래 좌표로

                    if y > color_r[i][2]:                               # 만일 y 좌표가 구역을 벗어나면
                        break                                           # i 번째 빨간 구역 순회를 종료

        print(f"#{tc} {cnt}")                                           # 결과 출력