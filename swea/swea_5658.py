# 4회전 시 0회전과 같아짐
# N//4개로 자르고 10진수로 변환 시 가장 큰 값을 업데이트 해줌
# deque 를 사용하는게 나으려나

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    number = list(input())
    cnt = N//4
    pw_li = []
    for i in range(cnt):
        for j in range(0, N-cnt+1, cnt):
            pw = ""
            for k in range(j, j + cnt):
                pw += number[k]
            if pw not in pw_li:
                pw_li.append(pw)
        tmp = number.pop()
        number = [tmp] + number

    ans = []
    while pw_li:
        num = pw_li.pop()
        b = int(num, 16)
        ans.append(b)
    ans.sort(reverse=True)
    print(f"#{tc} {ans[K-1]}")
