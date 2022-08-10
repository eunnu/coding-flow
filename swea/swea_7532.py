T = int(input())

for tc in range(1, T+1):
    S, E, M = map(int, input().split())
    ans = 0
    year = 0
    while True:                                         # 무한 루프
        ans = 365*year + S                              # S 연도를 기준으로 잡아야 그나마 반복 수를 줄일 수 있다..
        if (ans-E) % 24 == 0 and (ans-M) % 29 == 0:     # 만약 365*year + S 년을 기준으로 각 E, M을 빼고 각 최대 일수로 나눈 나머지가 0 이라면
            break                                       # 반복문 종료
        year += 1                                       # 연 수를 올려줌

    print(f"#{tc} {ans}")
