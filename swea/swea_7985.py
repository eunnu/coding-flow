from turtle import right


T = int(input())

for tc in range(1, T+1):

    k = int(input())
    tree_li = list(map(int, input().split(' ')))

    tree = [] # 마지막 트리 단 비교를 위한 리스트
    temp = 0

    for i in range(k, 1, -1):
        j = 2**i - 1 
        if i == k: # 처음 최상위 경우
            tree.append(tree_li[j//2])
            print(tree_li[j//2])
            temp = j//2 # 최상위 위치

        elif i > 0: # 두번째 ~ 마지막 전 단
            # 왼쪽
            tree.append(tree_li[j//2])

            print(tree_li[j//2] , end="")
            #오른쪽
            tree.append(tree_li[2*temp - j//2])

            print(tree_li[2*temp - j//2])
            temp = 2*temp - j//2
    # 마지막 단 출력
    for i in tree_li:
        if i in tree: continue
        tree.append(i)
        print(i, end="")
        
    print()



        