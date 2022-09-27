def merge_sort(in_li):
    if len(in_li) == 1:
        return in_li

    mid = len(in_li) // 2

    l_h = in_li[:mid]
    r_h = in_li[mid:]

    le = merge_sort(l_h)
    ri = merge_sort(r_h)

    return merge(le, ri)


def merge(left, right):
    global cnt
    res = [0]*(len(left)+len(right))

    ldx = rdx = idx = 0
    if left[-1] > right[-1]:
        cnt += 1

    while ldx < len(left) and rdx < len(right):
        if left[ldx] <= right[rdx]:
            res[idx] = left[ldx]
            ldx += 1
            idx += 1
        else:
            res[idx] = right[rdx]
            rdx += 1
            idx += 1

    while ldx < len(left):
        res[idx] = left[ldx]
        ldx += 1
        idx += 1
    while rdx < len(right):
        res[idx] = right[rdx]
        rdx += 1
        idx += 1

    return res


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    ans = merge_sort(arr)

    print(f"#{tc} {ans[N//2]} {cnt}")