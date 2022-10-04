# 주어진 리스트에서 각 보석으로 나눈 나머지 값이 0 인 경우만 보석의 가치를 더해줍니다.
# 시간을 줄이기 위해 받은 인덱스 위치 부터 반복문을 진행해 줍니다.
# 가치의 최대치는 매번 업데이트를 해줍니다.

def sol(jdx, cnt):
    global ans
    if cnt > M:
        return

    if ans < cnt:
        ans = cnt

    for idx in range(jdx, N):
        if not visit[idx]:
            for jj in jam_li:
                if not jam[idx] % jj:                   # 보석의 배수인지 확인 해 주고 배수라면 진행
                    visit[idx] = 1
                    sol(idx, cnt + jam[idx])
                    visit[idx] = 0


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    jam = list(map(int, input().split()))
    jam_li = [4, 6, 7, 9, 11]
    ans = 0
    visit = [0] * N
    for i in range(N):
        for j in jam_li:
            if not jam[i] % j:                          # 배 수 인지 확인해 줍니다.
                visit[i] = 1
                sol(i, jam[i])
                visit[i] = 0

    print(f"#{tc} {ans}")