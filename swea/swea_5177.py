# 재귀로 풀거임
# 부모 자식간인지 확인을 하고 만약 부모보다 자식이 크면 바꿔줄거임
# 마지막 노드까지 돌거임
# 부모를 돌려면 int(n/2) : 이때 n 은 자식 노드임


def heap(n):
    if n < 1:
        return

    if li[int(n/2)] > li[n]:
        li[int(n/2)], li[n] = li[n], li[int(n/2)]

    heap(int(n/2))


T = int(input())

for tc in range(1, T+1):
    M = int(input())
    li = [0] + list(map(int, input().split()))

    for i in range(2, M+1):
        heap(i)

    ans = 0
    while M >= 1:
        ans += li[int(M/2)]
        M = int(M/2)
    print(f"#{tc} {ans}")

