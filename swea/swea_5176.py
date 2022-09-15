# 완전 이진으로 풀거임
# 왼쪽인 경우 : 2 * n
# 오른쪽인 경우 : 2 * n + 1
# 왼쪽 돌고 나올 때 찍음


def inorder(n):
    if n > M:
        return

    inorder(2*n)
    tree.append(n)
    inorder(2*n+1)


T = int(input())

for tc in range(1, T+1):
    M = int(input())
    parent, node = 0, 0
    tree = [0]
    inorder(1)
    for idx in range(M+1):
        if tree[idx] == 1:
            parent = idx
        if tree[idx] == M//2:
            node = idx

    print(f"#{tc} {parent} {node}")

