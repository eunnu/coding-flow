def int_str(n):
    ans = ''                            # 정답을 넣어 줄 변수
    minus = ''                          # 음수 일 경우 -를 붙여 줄 변수
    if n < 0:                         # 음수 일 경우
        minus = chr(45)                 # -를 넣어줌
        n *= -1                       # 양수로 바꾸어 줌

    while n != 0:                     # num 을 더이상 나눌 수 없을 때 까지
        a = n % 10                    # 10으로 나눈 나머지 값을
        ans = chr(48+a) + ans           # 아스키 코드로 변환하여 앞에 넣어준다. -> 뒤에서부터 나누니까
        n = n//10                   # num 을 10으로 나눈다.

    ans = minus + ans                   # 정답에는 마이너스와 숫자를 더해준다.
    print(f"#{tc} {ans} {type(ans)}")   # 결과 출력

T = int(input())                        # 테스트 케이스 수를 입력받음

for tc in range(1, T+1):                # 1부터 T까지 반복
    num = int(input())                  # 숫자를 입력 받음

    int_str(num)