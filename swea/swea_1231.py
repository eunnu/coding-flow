'''
가장 왼쪽은 2**n 이므로 100 이하의 리스트를 만들어 해당 번호의 정점부터 시작한다.
'''
import sys
sys.stdin = open("input.txt", "r")


def dfs(idx):
    global ans
    if len(tree[idx]) == 2:
        if not visited[idx][1]:
            ans += tree[idx][1]
        visited[idx][1] = 1
        return

    else:
        dfs(int(tree[idx][2]) - 1)
        if not visited[idx][1]:
            ans += tree[idx][1]
            visited[idx][1] = 1
        if len(tree[idx]) == 3:
            return
        else:
            dfs(int(tree[idx][3]) - 1)
            return


for tc in range(1, 2):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]

    number = ['64', '32', '16', '8', '4', '2']

    ans = ''
    visited = [[0]*4 for _ in range(N)]
    for num in number:
        for j in range(N):
            if num in tree[j]:
                dfs(j)

    print(f"#{tc} {ans}")

