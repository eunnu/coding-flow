'''
가장 아래에 있는 주사위의 모든 면을 돌면서 마주보는 두 면을 제외한 면들 중 가장 큰 수를 더해주고
그 마주보는 면의 수와 닿는 주사위의 숫자를 확인해주면서 큰 값을 찾는다
일단 시도해보고 시간초과가 뜨면 다른 방법을 생각해 보는 걸로..
'''
N = int(input())
rand = []
ans = 0
for i in range(N):
    rand.append(list(map(int, input().split())))

a = [5, 3, 4, 1, 2, 0]
top, bottom = 0, 0     # 위, 아래 의 숫자를 넣어 줄 변수
for i in range(6):     # 가장 아래의 주사위를 돌거임
    visit = [[0] * 6 for _ in range(N)]
    bottom, top = rand[0][i], rand[0][a[i]]
    visit[0][i], visit[0][a[i]] = 1, 1
    maxi = 0            # 옆 면의 합을 넣어줄 변수

    for j in range(1, N):       # 2번째 주사위 부터 돌아 줄 거임
        for k in range(6):
            if rand[j][k] == top:
                bottom, top = rand[j][k], rand[j][a[k]]
                visit[j][a[k]], visit[j][k] = 1, 1
                break

    maxi = 0
    for j in range(N):
        tmp = 0
        for k in range(6):
            if not visit[j][k] and tmp < rand[j][k]:
                tmp = rand[j][k]
        maxi += tmp
    if maxi > ans:
        ans = maxi

    if ans < maxi:
        ans = maxi

print(ans)