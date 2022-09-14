'''
열을 돌면서 방문한 곳을 표시
방문 한 곳을 다시 배열에 표기
'''


def bfs(idx):
    for j in range(N):
        if not visited[j] and arr[idx][j]:
            visited[j] = 1
            bfs(j)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = [[0]*N for _ in range(N)]
for i in range(N):
    visited = [0]*N
    bfs(i)

    for j in range(N):
        if visited[j]:
            ans[i][j] = 1

for i in range(N):
    for j in range(N):
        if j == N-1:
            print(ans[i][j], end="")
        else:
            print(ans[i][j], end=" ")
    print()
