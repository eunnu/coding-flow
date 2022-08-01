import sys
sys.stdin = open("swea\input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split(' '))
    
    num = []
    for i in range(N):
        num.append(list(map(int, input().split(' '))))

    ans = []
    for i in range(N):
        sum_num = 0
        for j in range(M):
            sum_num += num[i][j]
        ans.append(sum_num)

    ans.sort(reverse=True)
    print(ans)
    res = 1
    for i in range(1, N):
        if ans[i] == ans[i-1]:
            res += 1
        else:
            break
    
    print(f'#{test_case} {res} {ans[0]}')
         
