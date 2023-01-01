# 1다음 00~ 1 / 1 다음 1 / ~ 01 / 이 만족해야 함
# 시작은 100 or 01 이어야 함
num = input()
flag = False

while num != '':
    if num[0] == '1':       # 시작이 100 인 경우
        if len(num) > 2 and num[:3] == '100':
            a = 2
            if num == '100':    # 100이 끝인 경우 NOISE
                flag = False
                break
            while True:         # 100으로 시작하는데 0이 3개 이상일 때,
                a += 1
                if a < len(num) and num[a] == '1':
                    flag = True
                    break
                if a > len(num):
                    break
            if flag:            # 0이 계속 되다가 정상적으로 1을 만났을 경우
                if a+2 < len(num) and num[a:a+3] == '100':      # 1000100 같은 경우
                    flag = False
                    break
                while True:         # 1이 계속 반복 되는 경우
                    a += 1
                    if a > len(num):
                        break
                    if a < len(num) and num[a] == '0':
                        if a+1 < len(num) and num[a-1:a+2] == '100':
                            a -= 1      # 만약 1이 계속 되다가 100으로 시작할 수도 있으니까
                        break           # 예를 들면, 10001111/1001 이런 경우
            else:
                flag = False
                break
            num = num[a:]
        else:
            flag = False
            break
    else:           # 01 인 경우는 01만 잘라주면 됨
        if len(num) > 1 and num[:2] == '01':
            num = num[2:]
        else:       # 0으로 시작하는데 00이거나 하는 경우
            flag = False
            break

if not flag:
    print('NOISE')
else:
    print("SUBMARINE")