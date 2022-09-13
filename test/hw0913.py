'''
재귀로 입력의 0 부터 짝수만 돌면서 해당 정점과 연결된 점들을 넣어줌
'''


def point(idx):                                             # 재귀를 돌건데
    for cur in range(1, 2*N-1, 2):                          # tree 리스트를 돌아 주면서
        if tree[cur - 1] == idx and not map_tree[cur]:      # 연결이 되어 있는지 확인 하는데 방문한 적이 없어야 하고
            idx = tree[cur]                                 # 조건을 만족한다면 현재 위치를 업데이트 해주고
            map_tree[cur] = 1                               # 방문했다고 표시 해주기
            stack.append(idx)                               # 정점을 넣어주고
            point(idx)                                      # 다음 정점을 찾으러 감
    return


N = int(input())
tree = list(map(int, input().split()))
map_tree = [0]*25                           # 방문 한 곳을 확인 해 줄 리스트
stack = []                                  # 정점을 넣어 줄 리스트
for i in range(N // 2 + 1):                 # 0부터 짝수 번째를 돌아 줌
    if not map_tree[2*i]:                   # 만약 방문 한 적이 없다면
        map_tree[2*i] = 1                   # 방문 했다고 표시 해주고
        if tree[2*i] not in stack:          # 정점을 넣어 준 적이 없다면
            stack.append(tree[2*i])         # 정점 표시 해주고
        point(tree[2*i])                    # DFS 재귀를 돌아줌

print(*stack)