from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

N = int(stdin.readline())
fruit = list(map(int, stdin.readline().split(" ")))
fruit_cnt = [0]*10


def solution(left, right, cnt, res, kind):
    if right >= N:
        return res

    if not fruit_cnt[fruit[right]]:
        kind += 1
    cnt += 1
    fruit_cnt[fruit[right]] += 1

    while kind > 2:
        cnt -= 1
        fruit_cnt[fruit[left]] -= 1
        if not fruit_cnt[fruit[left]]:
            kind -= 1
        left += 1

    res = max(res, cnt)

    return solution(left, right + 1, cnt, res, kind)


print(solution(0, 0, 0, 0, 0))