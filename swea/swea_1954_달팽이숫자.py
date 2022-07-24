test_case = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(test_case):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(0)
    max = n * n
    x , y, dir, cnt = 0, 0, 0, 2
    arr[0][0] = 1

    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end = ' ')
    #     print()
    
    while cnt <= max:
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        if(nx < 0 or ny < 0 or nx >= n or ny >= n or arr[ny][nx]):
            dir += 1
            if dir == 4: 
                dir = 0
            continue

        arr[ny][nx] = cnt
        cnt += 1
        x, y = nx, ny

    print('#%d'%(i+1))    
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
        print()

