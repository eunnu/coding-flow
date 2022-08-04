T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    temp = a + b
    while True:
        if temp < 24: break
        else:
            temp = temp - 24
            
    print(f'#{tc} {temp}')