T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())

    cnt = 0
    i = 0
    while True:
        # 종료 조건 : 남은 A의 길이가 B의 길이보다 작을 경우 반복문 탈출
        if len(A) < len(B):
            break

        '''
        ex) A : asakusa //  B : sa
        i == 0 -> else
        i == 1 -> A[1:1+2] = sa -> cnt = 1, i = 3
        i == 3 -> else
        i == 4 -> A[4:4+2] = sa -> cnt = 2, i = 6
        break
        '''

        if A[i:i+len(B)] == B:
            i = i+len(B)
            cnt += 1
        else:
            i += 1

    # 만약 B가 존재한다면 A 길이에서 B 길이의 cnt 만큼 곱한 값을 빼주고 cnt 를 다시 더해줌
    ans = len(A) - len(B)*cnt + cnt
    print(f"#{tc} {ans}")


