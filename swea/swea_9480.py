# 맞은 코드

T = int(input())

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for tc in range(1, T + 1):
    N = int(input())


    def check():
        global res
        comb_st = ''
        temp_num = 0
        for idx in range(len(visited)):
            if visited[idx]:
                comb_st += word[idx]

        te = ''
        for alphabet in alpha:
            if alphabet in comb_st:
                te += '1'

        if te == '11111111111111111111111111':
            res += 1


    def comb(idx, cnt, num):
        if num == cnt:
            check()
            return
        for comb_idx in range(idx, len(visited)):
            if visited[comb_idx]:
                continue
            visited[comb_idx] = 1

            comb(comb_idx, cnt + 1, num)
            visited[comb_idx] = 0


    word = []
    for _ in range(N):
        temp = input()
        word.append(temp)

    comb_li = []
    visited = [0] * N
    res = 0

    for i in range(1, N + 1):
        comb(0, 0, i)

    print(f'#{tc} {res}')