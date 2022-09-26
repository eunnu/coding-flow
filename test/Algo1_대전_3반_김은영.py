# 리스트를 순회하면서 이전보다 낮아지면 카운트
# 순회했던 봉우리의 높이를 계속 업데이트 해주면서 그 값보다 작아지는 순간 카운트
# 높아지다가 낮아지는 건 flag 로 확인
# 계속 낮아지면 flag 는 계속 False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mount = list(map(int, input().split()))

    ans = 0
    if N > 1:                                   # N의 길이가 1보다 큰경우
        if mount[0] > mount[1]:                 # 인덱스 에러를 방지 해주기 위한 0번 idx 값 확인
            ans += 1
        idx = 1
        flag = False
        if mount[0] == mount[1]:                # ex) 7 7 5 2 4 3 과 같은 경우 위의 조건 만으로는 해결 할 수 없음
            for i in range(1, N):
                if mount[0] != mount[i]:        # 처음과 높이가 같지 않을 때,
                    if mount[0] > mount[i]:     # 봉우리라면
                        flag = True             # 다음 반복문에서 카운트 할 수 있게 설정
                        idx = i                 # 해당 위치부터 순회할 수 있게 해줌
                        break

        for i in range(idx, len(mount)):        # 위의 조건문을 돌고 왔으면 2번 idx 에서 시작, 아니라면 1번 idx 에서 시작
            if mount[i] > mount[i - 1]:         # 만약 현재 위치가 다음 위치보다 크다면
                flag = True                     # 봉우리 일 수 있다.

            if mount[i] < mount[i - 1] and flag:    # 현재보다 다음 위치가 더 작은데 봉우리 일 수 있다고 한다면 봉우리
                ans += 1                            # 카운트 해주고
                flag = False                        # 이제 봉우리 다시 찾으러 감

        if flag:                                    # 마지막 idx 가 봉우리라면 카운트
            ans += 1
    else:                                           # N이 1 인 경우
        ans = 1

    print(f"#{tc} {ans}")