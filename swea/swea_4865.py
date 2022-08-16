T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()

    ans = 0                 # 정답 변수 선언
    for i in N:             # N을 순회
        cnt = 0             # N의 개수를 카운트 해줄 변수
        for j in M:         # M을 순회
            if i == j:      # 만약 N[i] == M[j]
                cnt += 1    # 카운트

            if cnt > ans:   # 카운트 값이 가장 큰 값이라면
                ans = cnt   # 카운트가 정답

    print(f"#{tc} {ans}")