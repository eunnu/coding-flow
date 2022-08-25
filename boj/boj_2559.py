'''
처음엔 슬라이싱으로 풀었으나 시간 초과..
슬라이딩 윈도우로 풀어야 시간초과가 안난다.
더한값에서 전 값을 빼주고 뒤의 값을 더해주면서 최대값 업데이트
'''
N, K = map(int, input().split())
number = list(map(int, input().split()))

sum_num = sum(number[:K])    # 초기 값 세팅
ans = sum_num
idx = 0   # 빼 줄 인덱스 값
for i in range(K, N):
    sum_num = sum_num - number[idx] + number[i]
    idx += 1
    if ans < sum_num:
        ans = sum_num

print(ans)

'''
ex)
10 5
3 -2 -4 -9 0 3 7 13 8 -3

3 ~ 0 까지 더한 값 : -12
idx = 0
k = 5 -> number[k] = 3, number[idx] = 3
i == 5
-12 - 3 + 3 = -12
i == 6
-12 + 7 - (-2) = -3
i == 7
-3 + 13 - (-4) = 14
i == 8
14 + 8 - (-9) = 31
i == 9
31 + (-3) - 0 = 28
'''