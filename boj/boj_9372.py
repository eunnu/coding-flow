'''
가장 왼쪽은 2**n 이므로 100 이하의 리스트를 만들어 해당 번호의 정점부터 시작한다.
1을 만나면 오른쪽을 도는 방법으로 재귀를 돈다.
'''


def right(depth, res):



def left(idx, res):
    if idx == '1':
        right(tree[0][3], res)
    for i in range(N):
        if len(tree[N]) == 2:
            res += tree[N][1]
            return
        for j in range(len(tree[i])):
            if



for tc in range(1, 11):
    N = int(input())
    tree = [list(map(input().split())) for _ in range(N)]

    number = [64, 32, 16, 8, 4, 2]

    visited = []
    ans = ''
    for num in number:
        if int(num) in tree:
            visited.append(num)
            left(num, ans)



