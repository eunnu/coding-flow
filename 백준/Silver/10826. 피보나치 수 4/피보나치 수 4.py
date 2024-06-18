from sys import stdin

N = int(stdin.readline())
pib = [0, 1]
if N > 2:
    res = 1
    for i in range(3, N+1):
        tmp = res
        res += pib[-1]
        pib[-1] = tmp
    
    print(res)
else:
    if N == 0:
        print(0)
    else:
        print(1)