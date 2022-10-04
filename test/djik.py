# # SWEA 5251 최소 이동 거리 풀이
#
# def dijkstra():
#     dist = [987654321] * (V+1)
#     dist[0] = 0  # 여기 start 점을 넣어주면 됨.
#     visited = [False] * (V+1)
#
#     for _ in range(V+1):
#         min_idx = -1
#         min_value = 987654321
#
#         for i in range(V+1):  # 일단 현재 dist 배열에서 visited 안된애들 중 가장 노드 찾는 로직
#             if not visited[i] and dist[i] < min_value:
#                 min_idx = i
#                 min_value = dist[i]  # 갱신!
#
#         visited[min_idx] = True  # 가장 작은애로 이동할거니까 visited 넣어주고
#         # 요거 주석 풀어서 visted, dist 찍어볼것!
#         # print(visited, dist)
#
#         # 이제 그 선택된 점에서부터 갈 수 있되, 그 가중치를 더하더라도 더 짧음을 보장한다면 dist 배열 갱신
#         for i in range(V+1):
#             if not visited[i] and dist[i] > adj[min_idx][i] + dist[min_idx]:
#                 dist[i] = adj[min_idx][i] + dist[min_idx]
#
#     return dist[V]  # 도착점
#
#
# for tc in range(1, int(input())+1):
#     V, E = map(int,input().split())
#
#     adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌
#
#     for i in range(E):  # 인접행렬 만들기
#         st, ed, w = map(int, input().split())
#         adj[st][ed] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화
#
#     print("#{} {}".format(tc, dijkstra()))


# SWEA 5251 최소 이동 거리 풀이
import heapq


def dijkstra():
    dist = [987654321] * (V+1)
    visited = set()  # 효율화를 위한 셋
    heap = []  # 빈 리스트 하나 생성해서 최소힙 자료구조로 활용
    heapq.heappush(heap, (0, 0))  # (거리, 노드번호)

    while heap:  # 힙이 빌때까지 돌아라
        distance, node = heapq.heappop(heap)  # 거리와 노드번호를 뽑고 (뽑힌 순간 최소 거리로 뽑혔을 것)
        if node not in visited:  # visited 없는 경우에 한해서 + visited 되지 않은 경우는 바로 다음 힙팝이 실행될 것!
            dist[node] = distance  # 최소힙에서 뽑았으니까 바로 그녀석의 distance가 최소 이동 거리일것
            visited.add(node)  # visited 도장을 찍어준다

            for destination in range(V+1):  # 현재의 node에서 갈 수 있는 destination을 모두 체크할건데,
                # 아직 방문하지 않았어야 함과 동시에
                # 목적지까지의 기존 이동거리라고 생각했던 것 > 내 위치까지의 이동거리 + 내 위치로부터 목적지까지의 이동거리를 만족하면
                if destination not in visited and dist[destination] > adj[node][destination] + dist[node]:
                    heapq.heappush(heap, (adj[node][destination] + dist[node], destination))  # 최소힙에 넣어라!

    return dist[V]


for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌

    for i in range(E):  # 인접행렬 만들기
        st, ed, w = map(int, input().split())
        adj[st][ed] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print("#{} {}".format(tc, dijkstra()))