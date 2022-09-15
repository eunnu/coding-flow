'''
tree 를 돌면서 부모가 M 인 자식 노드를 stack 에 넣어주고
그 노드의 자식 노드를 찾아서 append 해준다.
pop 할 때 마다 카운트 해준다. 자기 자신도 포함
'''


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))

    stack = [M]                     # 자기 자신을 먼저 넣어줌(M)
    visited = [0]*(2*N)             # 방문 확인
    cnt = 0                         # 카운트 초기화
    while stack:                    # 자식 노드가 없을 때 까지
        node = stack.pop()
        cnt += 1                    # 포함되는 서브 트리 카운트

        for i in range(N):
            if tree[2*i] == node:   # 만약 부모 노드인데
                if not visited[2*i] and (not visited[2*i+1]):   # 부모와 자식이 방문한 적이 없다면
                    stack.append(tree[2*i + 1])                 # 자식 노드를 스택에 넣어주고
                visited[2*i], visited[2*i+1] = 1, 1             # 방문 표시

    print(f"#{tc} {cnt}")