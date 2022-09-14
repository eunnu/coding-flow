'''
dfs로 풀거임
방문한 적이 없어야 하고 직 사각형이 그려져 있으면 안된다.
사각형이있는 부분을 1로 표기하고 없는 부분을 0으로 하는 배열을 생성
전체 배열을 돌면서 dfs로 영역을 카운트 해줌
그 카운트 값을 새로운 리스트에 넣어주고 오름차순 이기 때문에 정렬을 해주어야 함
와우... recursion error 를 맛보았다..
'''


import sys
sys.setrecursionlimit(100000)


def dfs(y, x):
    global cnt
    visited.add((y, x))
    cnt += 1

    for dire in range(4):
        ny = y + dy[dire]
        nx = x + dx[dire]

        if 0 <= ny < M and 0 <= nx < N:
            if (ny, nx) not in visited:
                if not arr[ny][nx]:
                    dfs(ny, nx)
    return

M, N, K = map(int, input().split())

arr = [[0]*N for _ in range(M)]
area = [list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    x1, y1, x2, y2 = area[i]
    for j in range(y1, y2):
        for k in range(x1, x2):
            arr[j][k] = 1

visited = set()
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

ans = []
if K == 1:
    ans.append(N*M - (y2-y1)*(x2-x1))

else:
    for i in range(M):
        for j in range(N):
            if (i, j) not in visited:
                if not arr[i][j]:
                    cnt = 0
                    dfs(i, j)
                    ans.append(cnt)

ans.sort()
print(len(ans))
print(*ans)