'''
1. 가장 높은 곳의 위치를 전달
2. 모든 배열을 확인 할 때까지 dfs 함수를 반복한다.
    1) 보내주어야 할 인자 : 위치 (y, x) 한 번 깎았는지 확인 해 줄 (False) -> flag 로 받음, 현재 위치의 높이 height,
       카운트 해준 cnt 값, 이전 위치의 높이 compare (비교가 필요한 경우)

3. 4방향으로 dfs 를 돌 때, 높이가 같거나 높은 곳을 만났는데 기회가 있다면 현재 위치의 높이를 다음 칸에 같이 보내준다.
    기회가 없다면
   1) 같이 보내 준 높이와 앞으로 가야 할 곳이 전달 받은 높이와 같거나 높으면 현재까지 저장 된 카운트-1을 ans 리스트에 넣어준다.
   2) 같이 보내 준 높이와 앞으로 가야 할 곳의 높이의 차가 K 미만이면 flag 를 True 로 바꾸고 계속 진행한다.
   3) 만일, flag 가 true 인 상황에서 현재 위치의 높이보다 높거나 같은 곳을 마주하면 현재까지의 cnt 를 ans 에 넣어주고 return
   1) ~ 3) 반복
4. ans.sort() 후에 ans[-1] 을 출력해 준다.
'''


# 2
def dfs(y, x, flag, height, cnt, compare):
    global ans
    for direction in range(4):
        ny = y + dy[direction]
        nx = x + dx[direction]

        if 0 <= ny < N and 0 <= nx < N:             # 인덱스 범위
            if (ny, nx) not in visited:             # 방문한 적이 없어
                if flag:                            # 기회를 써버린 경우
                    if mount[ny][nx] < height and height > compare:   # 가운데가 우뚝 선 경우
                        if compare - mount[ny][nx] <= 1:                # 양 옆의 산의 높이 차이가 1 이하인 경우
                            if ans < cnt-1:
                                ans = cnt-1
                                return
                        else:                                           # 양 옆의 산의 높이 차이가 k 미만인 경우
                            for kdx in range(1, K):
                                if mount[ny][nx] < height-kdx < compare:
                                    visited.add((ny, nx))
                                    dfs(ny, nx, flag, mount[ny][nx], cnt+1, height)
                                    visited.discard((ny, nx))

                            if ans < cnt:
                                ans = cnt
                                return

                    elif height <= mount[ny][nx]:
                        if ans < cnt:
                            ans = cnt
                            return

                    else:
                        visited.add((ny, nx))
                        dfs(ny, nx, flag, mount[ny][nx], cnt+1, height)
                        visited.discard((ny, nx))
                else:                                                                   # 기회가 있다
                    if mount[ny][nx] >= height:                                         # 기회를 사용하겠다
                        visited.add((ny, nx))
                        dfs(ny, nx, True, mount[ny][nx], cnt+1, height)
                        visited.discard((ny, nx))
                    else:                                                               # 스무스 하다.
                        visited.add((ny, nx))
                        dfs(ny, nx, flag, mount[ny][nx], cnt+1, height)
                        visited.discard((ny, nx))
    return


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    mount = [list(map(int, input().split())) for _ in range(N)]
    high = max(map(max, mount))
    ans = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if high == mount[i][j]:
                # 1
                visited = set()                 # 새로운 등산로를 찾을 때 마다 생성 해 주는 것이 낫다.
                visited.add((i, j))
                dfs(i, j, False, high, 1, -1)

    # 4
    print(f"#{tc} {ans}")
