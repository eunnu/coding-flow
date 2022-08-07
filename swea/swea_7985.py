from turtle import right


T = int(input())

for tc in range(1, T+1):
    
    k = int(input())
    tree_li = list(map(int, input().split(' ')))    
    
    ans = []

    ans.append([(2**k-1)//2]) # 0번째
    for i in range(2, k + 1):
        num = 2**(k - i)
        ans.append([]) # 1번째

        for j in range(len(ans[i-2])):
            ans[i-1].append(ans[i-2][j] - num)
            ans[i-1].append(ans[i-2][j] + num)

    print(f'#{tc}', end = (" "))
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(tree_li[ans[i][j]], end=" ")
        print()
    


        