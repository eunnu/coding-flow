T = int(input())                        # 테스트 케이스 수를 입력받음

for tc in range(1, T+1):                # 1부터 T까지 반복
    s = input()                         # 문자열을 입력 받음

    ans = ''                            # 정답 문자열을 선언
    for i in range(len(s)-1, -1, -1):   # 문자열의 길이만큼 뒤에서 부터 반복
        ans += s[i]                     # 해당 문자를 정답 문자열에 더해줌

    print(f"#{tc} {ans}")               # 결과 출력