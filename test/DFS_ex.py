N, M = map(int, input().split())

arr = [[0]*(N+1) for _ in range(N+1)]
map_input = list(map(int, input().split()))

for i in range(M):
    arr[map_input[2*i]][map_input[2*i+1]] = 1
    arr[map_input[2*i+1]][map_input[2*i]] = 1

stack = []
visited = []
stack.append(map_input[0])

while stack:
    num = stack.pop()
    if num not in visited:
        visited.append(num)

    for i in range(M):
        if num == i or i in visited:
            continue
        if arr[num][i]:
            stack.append(i)

print("", *visited)