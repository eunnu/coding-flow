def game(s1, s2, s3):


N, M, D = map(int, input().split())
area = []
num = []
for _ in range(N):
    area.append(list(map(int, input().split())))

for i in range(M):
    tmp = 0
    for j in range(N):
        tmp += area[j][i]
    num.append([tmp, i])
num.sort(reverse=True)

for i in range(M-2):
    game(num[i][1], num[i+1][1], num[i+2][1])