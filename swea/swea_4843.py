T = int(input())                              # 테스트 케이스 수를 입력받음

for tc in range(1, T+1):                      # 1부터 T까지 반복
    N = int(input())                          # 배열의 크기를 입력 받음
    arr = list(map(int, input().split()))     # 배열을 입력 받음

    arr.sort()                                # 오름차순 정렬

    ans = []                                  # 정답 배열
    num = 0                                   # 앞과 뒤를 번갈아야 하기 때문에 기준점 선언
    ans.append(arr[-1])                       # 맨 앞에 가장 큰 수를 넣어줌
    for i in range(1, 10):                    # 정답을 10개까지 출력이기 때문에 10 까지만 반복
        if not i % 2:                         # 만약에 짝수라면
            num += 1                          # num += 1

        if i % 2:                             # 만약 홀수라면
            ans.append(arr[num])              # 작은 값들을 넣어줌
        else:                                 # 만약 짝수라면
            ans.append(arr[-num-1])           # 큰 값들을 넣어준다.

    print(f"#{tc}", end=' ')                  # 결과 출력
    for i in range(10):
        print(ans[i], end=' ')
    print()