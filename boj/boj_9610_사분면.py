ans = {'Q1' : 0, 'Q2' : 0, 'Q3' : 0, 'Q4' : 0, 'AXIS' : 0}
n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x == 0 or y == 0:
        ans['AXIS'] += 1
    elif x < 0 and y > 0:
        ans['Q2'] += 1
    elif x > 0 and y > 0:
        ans['Q1'] += 1
    elif x < 0 and y < 0:
        ans['Q3'] += 1
    else:
        ans['Q4'] += 1

for i in ans:
    print(f'{i}: {ans[i]}')

