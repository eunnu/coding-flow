#  솔루션 코드를 작성합니다.
# 뒤에서 부터 돌면서 부모의 노드에 자식 값을 더해준다.


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)

    for node in range(M):
        num, value = map(int, input().split())
        tree[num] = value

    comp = int(N/2)
    mid = 0
    for i in range(N, -1, -1):
        tree[int(i/2)] += tree[i]

    print(f"#{tc} {tree[L]}")
