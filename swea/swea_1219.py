for _ in range(10):
    tc, N = map(int, input().split())

    load_map = list(map(int, input().split()))         # 연속 되는 숫자 쌍을 리스트로 입력 받음

    stack = [0]                                        # 출발 점 : 0
    visited = [0]                                      # 0 은 방문 했음

    ans = 0

    while stack:
        start = stack.pop()                            # 출발 점은 stack[-1]

        if start not in visited:                       # 방문 한 적 없는 출발 점이면 visited 에 넣어줌
            visited.append(start)

        if start == 99:                                # 출발점이 도착점이 되면 길이 있으므로 1 로 넣어주고 break
            ans = 1
            break

        for i in range(0, len(load_map), 2):           # load_map 내에서 (출발, 도착)이 한 쌍이므로 2개 단위로 반복문을 돌려줌
            if load_map[i] == start:                   # 출발 점을 찾으면
                if load_map[i+1] not in visited:       # 방문 한 적이 있는 지 확인하고
                    stack.append(load_map[i+1])        # 방문 한 적 없다면 도착점을 stack 에 넣어준다.

    print(f"#{tc} {ans}")