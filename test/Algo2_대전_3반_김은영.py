# 전위 배열, 중위 배열, 후위 배열을 만들어
# 순서대로 가장 큰 값들을 출력한다.
def order(num):
    if num in li:               # 정점이라면
        if num not in A:
            A.append(num)
        order(2 * num)          # 왼쪽 으로 감
        if num not in B:        # 왼쪽 값이 없는데 중위에 없다면
            B.append(num)       # 넣어줌
        order(2 * num + 1)      # 오른쪽으로 감
        if num not in B:        # 오른 쪽 값이 없다면 중위에 없다면 넣어줌
            B.append(num)
        if num not in C:        # 왼쪽 값이 없다면
            C.append(num)       # 후위에 없다면 넣어줌


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = [i for i in range(1, N + 1)]

    A, B, C = [], [], []            # 전위, 중위, 후위
    order(1)                 # 전위, 중위, 후위를 함께 돌거임

    maxi = [0]
    for i in range(N):
        maxi.append(max(A[i], B[i], C[i]))      # 제일 큰 값 리스트를 만들어 줌

    ans = []
    for i in B:
        ans.append(maxi[i])                     # B가 중위 인덱스 순서이기 때문에 그대로 maxi 를 정렬해주면 답
    print(f"#{tc}", end=" ")
    print(*ans)

