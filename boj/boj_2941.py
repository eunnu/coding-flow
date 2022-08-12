kro = input()                                                                               # 문자열을 입력 받음

cnt = 0                                                                                     # 알파벳 수를 넣어줄 변수

num = 0                                                                                     # index 값을 변경 해 줄 변수
for i in range(len(kro)):                                                                   # kro 길이 만큼 반복
    if num != 0 and i < num:                                                                # 초기값과 변경 된 인덱스 값보다 작다면 continue
        continue

    if i+1 < len(kro) and kro[i] == 'c' and kro[i+1] == '=':                                # c= 인 경우
        cnt += 1                                                                            # 개수를 카운트
        num = i + 2                                                                         # 그 다음 알파벳 확인

    elif i+1 < len(kro) and kro[i] == 'c' and kro[i + 1] == '-':                            # c- 인 경우
        cnt += 1
        num = i + 2

    elif i+2 < len(kro) and kro[i] == 'd' and kro[i + 1] == 'z' and kro[i + 2] == '=':      # dz= 인 경우
        cnt += 1
        num = i + 3

    elif i+1 < len(kro) and kro[i] == 'z' and kro[i + 1] == '=':                            # z= 인 경우
        cnt += 1
        num = i + 2

    elif i+1 < len(kro) and kro[i] == 'd' and kro[i + 1] == '-':                            # d- 인 경우
        cnt += 1
        num = i + 2

    elif i+1 < len(kro) and kro[i] == 'l' and kro[i + 1] == 'j':                            # lj 인 경우
        cnt += 1
        num = i + 2

    elif i+1 < len(kro) and kro[i] == 'n' and kro[i + 1] == 'j':                            # nj 인 경우
        cnt += 1
        num = i + 2

    elif i+1 < len(kro) and kro[i] == 's' and kro[i + 1] == '=':                            # s= 인 경우
        cnt += 1
        num = i + 2
    else:                                                                                   # 그냥 알파벳인 경우
        cnt += 1

print(cnt)