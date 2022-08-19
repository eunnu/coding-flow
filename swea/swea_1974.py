'''
가로 함수 width
세로 함수 height
한 칸 함수 box
각 ans 를 return 받아 모든 ans 가 True 일 때 True
'''
def wh(num):
    check_x = [0]*10
    check_y = [0]*10
    for idx in range(9):
        if check_x[puzzle[num][idx]]:
            return 0
        else:
            check_x[puzzle[num][idx]] = 1

        if check_y[puzzle[idx][num]]:
            return 0
        else:
            check_y[puzzle[idx][num]] = 1
    return 1

def box(y, x):
    check = [0] * 10
    for idx_y in range(3):
        for idx_x in range(3):
            if check[puzzle[idx_y+y][idx_x+x]]:
                return 0
            else:
                check[puzzle[idx_y + y][idx_x + x]] = 1
    return 1

T = int(input())
for tc in range(1, T+1):
    puzzle = []
    for i in range(9):
        puzzle.append(list(map(int, input().split())))

    ans_w, ans_b, ans = 0, 0, 1
    for i in range(9):
        ans_w = wh(i)
        if not ans_w:
            ans = 0
            break

    flag = False
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            ans_b = box(i, j)
            if not ans_b:
                flag = True
                break
        if flag:
            break

    if not ans or not ans_b:
        ans = 0

    print(f"#{tc} {ans}")
