paper = []

N = int(input())

for i in range(N):
    paper.append(list(map(int, input().split())))
x = 0.5
y = 0.5
d = 0
for i in range(100):
    for j in range(100):
        nx = x + j
        ny = y + i
        visited = []  # 중복을 확인해주기 위한 리스트
        for k in range(N):
            if [ny, nx] in visited:  # 좌표를 리스트 형식으로 있는지 확인
                continue
            if paper[k][0] < nx < paper[k][0] + 10:  # 길이는 10 X 10 으로 동일 하기 때문에 좌표에 10 을 더해주면 됨
                if paper[k][1] < ny < paper[k][1] + 10:
                    visited.append([ny, nx])  # 좌표를 리스트 형식으로 넣어줌. idx 가 0.5 단위면 에러가 발생함
                    d += 1

print(d)