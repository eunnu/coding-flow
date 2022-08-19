'''
0~N 까지 인덱스 순열을 뽑아서 최소 합을 구한다.
'''
def perm(idx, acc):
    global ans
    if acc > ans:
        return
    if idx == N:
        if ans > acc:
            ans = acc
        return
    else:
        for i_idx in range(N):
            if visited[i_idx] == 0:
                visited[i_idx] = 1
                perm(idx+1, acc + arr[idx][i_idx])
                visited[i_idx] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    visited = [0]*N
    ans = 987654321
    perm(0, 0)

    print(f"#{tc} {ans}")