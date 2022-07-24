a = list(map(int, input().split(' ')))
a.sort()

cnt = 1

for i in range(2):
    if(a[i] == a[i+1]):
        cnt += 1

if cnt == 2: print(100*a[1]+1000)
elif cnt == 3: print(1000*a[0] + 10000)
else: print(a[2]*100)


