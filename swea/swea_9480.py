import itertools
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    sam = ''
    sam_li = []
    alpha = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0,
                'n' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
    for _ in range(N):
        sam = input()
        sam_li.append(sam)
            
    for i in range(N):
        for j in range(len(sam_li[i])):
            if sam_li[i][j] in alpha:
                alpha[sam_li[i][j]] += 1
                
    
    print(alpha)
    '''
    alpha_li = []
    for i in alpha.keys():
        if (alpha.get(i) - 1):
            alpha_li.append(i)

    ans = 0
    result = list(itertools.combinations((alpha_li),2))

    print(result)
    #print(f'#{tc} ')
    '''
            

