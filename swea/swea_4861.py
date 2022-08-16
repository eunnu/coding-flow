T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = []

    for i in range(N):
        arr.append(input())

    flag = False
    st = ''
    for i in range(N):                  # 전체 문자열의 크기만큼 반복
        for j in range(N-M+1):          # 전체 문자열의 크기에서 주어진 길이를 뺀 길이만큼 반복

            st = ''                     # 정답 문자열을 초기화
            st += arr[i][j:j+M]         # 주어진 길이만큼의 문자를 더해줌

            if st == st[::-1]:          # 그 문자열과 reverse 가 같다면 전체 반복문 종료
                flag = True
                break

            st = ''                     # 정답 문자열을 초기화
            for k in range(M):          # 주어진 길이만큼 반복
                st += arr[j + k][i]     # 세로 방향으로 문자를 문자열에 더해줌
            if st == st[::-1]:          # 해당 문자열과 reverse 가 같다면 전체 반복문 종료
                flag = True
                break
        if flag:                        # 최상위 반복문 종료
            break

    print(f"#{tc} {st}")