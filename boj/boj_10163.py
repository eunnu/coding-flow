'''
가로 1001
세로 1001
(0, 0) ~ (1001, 1001) 까지 반복하면서
해당 인덱스가 가장 위에 있는 색종이부터 포함이 되는지를 확인한다.
포함이 되는 색종이의 넓이에 +1 해준다.
'''

N = int(input())

paper = []
p_d = [0]*N

for i in range(N):
    paper.append(list(map(int, input().split())))

for i in range(1002):
    for j in range(1002):
        for k in range(N-1, -1, -1):
            if paper[k][0] <= j <= (paper[k][2] + paper[k][0] - 1):
                if paper[k][1] <= i <= (paper[k][3] + paper[k][1] - 1):
                    p_d[k] += 1
                    break

'''
ex)
N = 2
p_d = [0, 0]
paper = [[0, 0, 10, 10],        0번 색종이 : 0 <= 가로 <= 9 / 0 <= 세로 <= 9
         [2, 2, 6, 6]]          1번 색종이 : 2 <= 가로 <= 7 / 2 <= 세로 <= 7

i : 세로 / j = 가로
(0, 0) -> 1번 x 0번 o -> pd[0] += 1
(0, 1) -> 1번 x 0번 o -> pd[0] += 1
   `
   `
(2, 2) -> 1번 o break -> pd[1] += 1
(2, 3) -> 1번 o break -> pd[1] += 1
   `
   `
가장 위에 있는 색종이에 포함이 되면 넓이를 더해주고 자리를 옮겨준다
'''
for i in p_d:
    print(i)