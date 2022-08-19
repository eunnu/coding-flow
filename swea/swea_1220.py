import sys
sys.stdin = open("input.txt", "r")
T = 10
'''
위에서 내려가다가 빨강을 만나면 flag = True
더 내려가다가 flag 일 때 파랑을 만나면 cnt + 1 다시 flag = False
!flag 일 때 파랑을 만나면 지나가
빨강 1 파랑 2
'''
for tc in range(1, 11):
    N = int(input())

    table = []
    for i in range(100):
        table.append(list(map(int, input().split())))

    cnt = 0
    for x in range(100):
        flag = False
        for y in range(100):
            if table[y][x] == 1:
                flag = True
            if flag and table[y][x] == 2:
                cnt += 1
                flag = False

    print(f"#{tc} {cnt}")