import sys


# 더이상 나눌 수 없을 때까지 나누어 주어야 함.
# 가장 큰 곳에서 1사분면을 먼저 살펴서 작은 구역으로 들어가서 return


b_res, w_res = 0, 0


def solution(num, r, c):
    global b_res, w_res

    for y in range(r, r + num):
        for x in range(c, c + num):
            if card[r][c] != card[y][x]:
                solution(num//2, r, c)  # 1사분면
                solution(num//2, r + num//2, c)  # 3사분면
                solution(num//2, r, c + num//2)  # 2사분면
                solution(num//2, r + num//2, c + num//2)  # 4사분면
                return
    if card[r][c] == 1:
        b_res += 1
    else:
        w_res += 1
    return


N = int(input())
card = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
solution(N, 0, 0)
print(w_res)
print(b_res)

