def change_bin(num):
    a = bin(num-3)[2:]
    while len(a) < 7:
        a = '0' + a
    a = '1' + a
    return a


for _ in range(int(input())):
    N = int(input())
    st = ''
    ans = ''
    for _ in range(N//41 + 1):
        st += input()

    if len(st) == 2:
        ans = '00' + st
    else:
        tmp = dict()
        for i in range(0, len(st), 2):
            temp = st[i:i+2]
            if not tmp:
                tmp[temp] = 1
            elif tmp and temp in tmp:
                tmp[temp] += 1
            else:
                if tmp.values() > 2:
                    



    print(len(ans)//2)
    print(ans)