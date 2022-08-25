'''
피자를 빼서 확인하는 작업을 queue.pop(0) 이라고 하자.
치즈를 녹였을 때, 0 이 되면 새로운 피자를 넣고
다 안녹았으면 다시 append 해준다.
피자와 화덕을 둘 다 queue
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    oven = []                                   # 화덕 queue
    pizza = list(map(int, input().split()))

    number = 1                                  # 피자 번호
    for i in range(N):                          # 처음 피자를 화덕에 넣어주는 작업
        oven.append([number, pizza.pop(0)])     # 번호와 치즈의 양을 같이 넣어줌
        number += 1

    while len(oven) > 1:                        # 피자가 하나 남으면 반복문 종료
        [check, ch] = oven.pop(0)
        ch = ch//2
        if ch > 0:                              # 치즈가 다 안녹았으면 다시 넣어주고
            oven.append([check, ch])
        else:                                   # 치즈가 다 녹았는데
            if pizza:                           # 남은 피자가 있으면 넣어준다.
                oven.append([number, pizza.pop(0)])
                number += 1

    print(f"#{tc} {oven[0][0]}")                # 하나 남아있는 피자의 번호를 출력

