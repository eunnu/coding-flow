def perm(idx):
    if idx == N:
        print(a)
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                a[idx] = arr[i]
                perm(idx+1)
                visited[i] = 0


N = 3
arr = [i for i in range(N)]
visited = [0]*N
a = [0]*N
perm(0)
