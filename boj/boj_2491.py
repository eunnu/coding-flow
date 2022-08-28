'''
반복문 안에서 감소와 증가를 같이 확인해주어서 가장 큰 카운트 값 출력
만약 카운트 값이 3보다 작으면 2를 출력
'''

N = int(input())
number = list(map(int, input().split()))

b_cnt, s_cnt, ans = 1, 1, 0                 # 증가 카운트, 감소 카운트, 답

if N == 1:
    ans = 1

else:
    for i in range(1, N):
        if number[i] > number[i-1]:             # 증가하는 경우
            b_cnt += 1
            if ans < s_cnt:                     # 감소하는 경우가 답보다 큰 경우 답 업데이트 후 감소 카운트 초기화
                ans = s_cnt
            s_cnt = 1

        if number[i] < number[i-1]:             # 증가하는 경우가 답보다 큰 경우 답 업데이트 후 증가 카운트 초기화
            s_cnt += 1
            if ans < b_cnt:
                ans = b_cnt
            b_cnt = 1

        if number[i] == number[i-1]:            # 숫자가 같은 경우는 두 카운트 변수 증가
            b_cnt += 1
            s_cnt += 1

    if ans < b_cnt:
        ans = b_cnt
    if ans < s_cnt:
        ans = s_cnt
    if ans < 3:
        ans = 2

print(ans)