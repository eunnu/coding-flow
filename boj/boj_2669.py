'''
좌표 위를 돌면서 해당되는 구역이면 면적 + 1
면적을 구해야 하기 때문에 0.5, 0.5 를 기준으로 돌아줌
'''

sq = []

for i in range(4):
    sq.append(list(map(int, input().split())))
x = 0.5
y = 0.5
d = 0
for i in range(100):
    for j in range(100):
        nx = x + j
        ny = y + i
        visited = []  # 중복을 확인해주기 위한 리스트
        for k in range(4):
            if [ny, nx] in visited:  # 좌표를 리스트 형식으로 있는지 확인
                continue
            if sq[k][0] < nx < sq[k][2]:
                if sq[k][1] < ny < sq[k][3]:
                    visited.append([ny, nx])  # 좌표를 리스트 형식으로 넣어줌. idx 가 0.5 단위면 에러가 발생함
                    d += 1

print(d)