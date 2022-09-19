# 16 진수를 2 진수로 변환
# 그 값을 다시 10 진수로 변환


# 2 로 나누어 주고 그 나머지를 계속 앞에 붙여준다.
def hex_bin(n):
    global Bb
    temp = ''
    while n > 0:
        if n % 2:
            temp = "1" + temp
        else:
            temp = "0" + temp
        n //= 2

    if len(temp) < 4:
        while len(temp) < 4:
            temp = "0" + temp

    Bb += temp


T = int(input())
for tc in range(1, T+1):
    num = input()
    Bb = ''
    ans = []
    for i in num:
        if 48 <= ord(i) <= 57:
            hex_bin(int(i))

        else:
            tmp = ord(i) - 55
            hex_bin(tmp)

    d = 6
    tmp = 0
    for i in range(len(Bb)):
        if d == -1:
            ans.append(tmp)
            tmp = 0
            if len(Bb) - i > 6:
                d = 6
            else:
                d = len(Bb) - i - 1
        if Bb[i] == '1':
            tmp += (2**d)
        d -= 1

    ans.append(tmp)
    print(f"#{tc} ", end="")
    print(*ans)