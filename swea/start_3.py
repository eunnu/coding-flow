T = int(input())
for tc in range(1, T+1):
    num = input()

    Bb = ''
    # 2 진수로 변환해 주기 위해서는 10진수로 변환 후에 2 진수로 변환해야 함
    for i in num:
        tmp = int(i, base=16)
        a = bin(tmp)
        # 0bxxxx 로 변환되기 때문에 0b를 제외하고 해줌
        # 4자리로 맞춰 주어야 함
        a = a[2:]
        if len(a) < 4:
            while len(a) < 4:
                a = "0" + a
        Bb += a

    # 암호를 찾는 방법에는 리스트를 만들어 있는지 확인 해 주고 해당 index 를 넣어줌
    li = ["001101", "010011", "111011", "110001", "100011", "110111", "001011", "111101", "011001", "101111"]

    ans = []
    flag = True
    i = 0
    while flag:
        check = False
        tmp = Bb[i:i+6]
        for j in range(10):
            if tmp == li[j]:
                ans.append(j)
                check = True
                i += 6
        if not check:
            i += 1
        if i >= len(Bb):
            flag = False

    print(*ans)