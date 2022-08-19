'''
0~N 까지 인덱스 순열을 뽑아서 최소 합을 구한다.
'''
def perm(idx):
    global ans
    if idx == N:
        if ans > sum(ex):
            ans = sum(ex)
    else:
        for i_idx in range(N):
            if visited[i_idx] == 0:
                visited[i_idx] = 1
                ex[idx] = arr[idx][number[i_idx]]
                perm(idx+1)
                visited[i_idx] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    number = [i for i in range(N)]
    visited = [0]*N
    ex = [0]*N
    ans = 987654321
    perm(0)

    print(f"#{tc} {ans}")