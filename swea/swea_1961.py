T = int(input())
'''
어떻게 할거냐며는
90도 회전 함수 만들어서 세번 반복 해 줄건데
회전시킬 때 각 행을 str 형식으로 더해주고 열이 바뀔 때 마다 그걸 int 형식으로 바꿔서 list 에 넣어줄 거임
'''
def turn_90(num):
    turn = []
    for i_idx in range(N):
        a = []
        b = ''
        for j_idx in range(N-1, -1, -1):
            a.append(arr[j_idx][i_idx])
            b += str(arr[j_idx][i_idx])
        turn.append(a)
        ans[i_idx][num] = b

    for i in range(N):
        for j in range(N):
            arr[i][j] = turn[i][j]

for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    ans = [[0]*3 for _ in range(N)]
    for i in range(3):
        turn_90(i)

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end=" ")
        print()
