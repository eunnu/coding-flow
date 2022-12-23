# 길이를 8로 고정해 놓고, 끝에 :: 인경우와 맨 앞이 :: 인 경우를 예외로 두고
# 반복문을 돌려 길이가 4보다 밑이면 0을 추가해줌

a = list(input().split(':'))

if len(a) > 8:
    if a[0] == '':
        a = a[1:]
    elif a[-1] == '':
        a.pop()

while True:
    for i in range(8):
        b = a[i]
        if b == '' and len(a) < 8:
            while len(a) < 8:
                a.insert(i, '0000')
        while len(b) < 4:
            b = '0' + b
        a[i] = b
    if len(a) == 8:
        break

for i in range(8):
    for j in range(4):
        print(a[i][j], end='')
    if i < 7:
        print(':', end='')
