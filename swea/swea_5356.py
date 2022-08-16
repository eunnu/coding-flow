T = int(input())

for tc in range(1, T+1):

    us = [['-1']*15 for _ in range(5)]

    for i in range(5):
        st = input()
        for j in range(len(st)):
            us[i][j] = st[j]

    st = ''
    for i in range(15):
        for j in range(5):
            if us[j][i] == '-1':
                continue
            else:
                st += us[j][i]

    print(st)