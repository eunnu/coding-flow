def game(x):
    print(f'x: {x}, A의 리스트: {cnt_list[0][x]}, B의 리스트: {cnt_list[1][x]}')
    if x <= 0:
        print('D')
        return 'D'
    if cnt_list[0][x] == cnt_list[1][x]:
        game(x-1)
    return 'A' if cnt_list[0][x] > cnt_list[1][x] else 'B'


N = int(input())
for case_num in range(1, N+1):
    cnt_list = [[0]*5 for _ in range(2)]
    for AB in range(2):
        for num in list(map(int, input().split()))[1:]:
            cnt_list[AB][num] += 1
    print(game(4))