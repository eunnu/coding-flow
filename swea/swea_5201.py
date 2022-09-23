# 우선 트럭과 화물의 리스트를 정렬 해준다.
# 트럭을 돌면서 화물을 넣어주는데, 무게가 남으면 더 큰 화물을 넣어보고, 더해서 넣어본다.
# 트럭보다 화물이 커지는 순간 반환
# 각 트럭에서 가장 큰 무게들의 합을 구한다.


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                        # N : 화물, M : 트럭
    cont = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    cont.sort(reverse=True)
    truck.sort(reverse=True)

    visited = [0] * N
    ans = []
    for i in range(M):
        for j in range(N):
            if not visited[j]:
                if truck[i] >= cont[j]:
                    visited[j] = 1
                    ans.append(cont[j])
                    break

    print(f"#{tc} {sum(ans)}")
