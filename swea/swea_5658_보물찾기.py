t = int(input())

for tc in range(t):
    n, k = map(int, input().split(' '))
    pw = list(map(str,input()))

    pocket = []
    for _ in range(n//4): # 회전 횟수        
        for i in range(0,n,n//4): # 묶음 갯수
            temp = ''
            for j in range(n//4):
                temp = temp + pw[i+j]
            temp = int(temp, 16)
            pocket.append(temp)  
        pp = pw.pop()
        pw.insert(0, pp)

    pocket.sort(reverse = True)
    pocket = set(pocket)
    pocket = list(pocket)
    
       
    
    print(f'#{tc+1} {pocket[k-1]}')
