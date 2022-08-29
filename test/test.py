from collections import deque
T = int(input())

for tc in range(1, T + 1):
    big = int(input())
    maze = [list(map(int,input())) for _ in range(big)]
    row = -1
    col = -1
    d_r = [-1,0,1,0]
    d_c = [0,1,0,-1]
    flag = 0
    ans = 0
    end = 0

    q = deque()
    visited = deque()

    #2 찾기
    for i in range(big):
        for j in range(big):
            if maze[i][j] == 3:
                row = i        #출발하는 행의 인덱스
                col = j #출발하는 열의 인덱스
                end = 1
                break
        if end:
            break
    #출발하는 인덱스에서 좌표가 0인 인덱스를 추가시킴

    q.append([row,col,0])

    while q and flag == 0:
        #큐에서 빼서 상우하좌를 탐색해서 0이 있는 부분 좌표를 q에 넣는다.
        current = q.popleft()
        row = current[0]
        col = current[1]


        if [row,col] not in visited:
            visited.append([row,col])

        for direction in range(4):
            #좌표가 메이즈안에 있고 값이 0일 경우에 queue에 넣는다.
            if (0 <= row+d_r[direction] < big) and (0 <= col + d_c[direction] < big) and (maze[row+d_r[direction]][col+d_c[direction]] != 1):
                if maze[row+d_r[direction]][col+d_c[direction]] == 2:
                    ans = current[2]
                    flag = 1
                    break

                elif [row+d_r[direction], col + d_c[direction]] not in visited:
                    q.append([row+d_r[direction], col + d_c[direction],current[2]+1])
        print(q)


    print(f'#{tc} {ans}')