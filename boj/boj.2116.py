'''
마주 보는 면 끼리 묶으면 (A,F)(B,D)(C,E) 세 묶음이 나오는데 N 개의 주사위들의 중복 조합을 만들어
나머지 면 중에서 숫자가 제일 큰 면들의 합 중에 제일 큰 값을 출력한다.
'''
N = int(input())
rand = []
num = []
tmp = []
for i in range(N):
    rand.append(list(map(int, input().split())))
    tmp1 = [rand[i][0], rand[i][5]]
    tmp2 = [rand[i][1], rand[i][3]]
    tmp3 = [rand[i][2], rand[i][4]]
    tmp.append(tmp1)
    tmp.append(tmp2)
    tmp.append(tmp3)
    num.append(tmp[:])
    tmp.clear()

ans = 0
comb = []
for i in range(N-1):
    for j in range(i, N):
        comb.append([i, j])

for i in range()zzzzzzzzz