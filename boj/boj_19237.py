# 상어가 냄새를 뿌리고
# 1초마다 인접한 칸으로 이동 -> 냄새를 뿌림 -> K번 이동 후 사라짐
# 인접한 칸을 고를 때는 냄새가 없어야 함
# 이동 한 후 여러마리가 한 칸에 있으면 번호가 가장 작은 상어만 남음
# 각 상어마다 방향 우선순위가 주어진다.
# 상, 하, 좌, 우

N, M, K = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
di = list(map(int, input().split()))
