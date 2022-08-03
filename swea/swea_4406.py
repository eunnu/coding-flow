T = int(input())
for tc in range(1, T+1):
    ch = ['a', 'e', 'i', 'o', 'u']
    ans = ''
    st = input()

    for i in st:
        if i in ch:
            continue
        else:
            ans += i

    print(f'#{tc} {ans}')