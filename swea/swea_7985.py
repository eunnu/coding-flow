T = int(input())

for tc in range(1, T+1):
    
    k = int(input())
    tree_li = list(map(int, input().split(' ')))    
    
    ans = []

    ans.append([(2**k-1)//2])                   # 처음 중앙의 idx를 ans 리스트에 넣어줌             
    for i in range(2, k + 1):                   # i는 2 부터 k 까지 이므로 k + 1 까지 범위로 설정해줌
        num = 2**(k - i)                        # num 은 두 단의 차이를 넣어줄 변수 ex) k = 3 인 경우 -> 2**(k-2), 2**(k-3)
        ans.append([])                          # 단의 구분을 짓기 위한 리스트를 append 해줌

        for j in range(len(ans[i-2])):          # 전 단의 길이 만큼 반복문을 돌려줌
            ans[i-1].append(ans[i-2][j] - num)  # 중간값 - 1, 중간값 + 1 이므로 전 단의 길이만큼 해당 규칙을 반복해준다.
            ans[i-1].append(ans[i-2][j] + num) 

    print(f'#{tc}', end = (" "))                # 출력 양식을 지키기 위함
    for i in range(len(ans)):                   # ans 에는 idx 값이 저장되어 있기 때문에
        for j in range(len(ans[i])):            # ans의 길이만큼, 그 단의 길이만큼 반복해줌
            print(tree_li[ans[i][j]], end=" ")  # 해당 단의 길이만큼 tree_li 리스트 값을 한 줄로 출력
        print()                                 # 단이 끝나면 줄 바꿈
    


'''
K = 2 -> tree_li = [2, 1, 3] 일 경우

            1
        2       3

첫 단과 두번째 단의 idx 차이가 2**0승 -> 2**(k-2)

k = 3 -> tree_li = [3, 2, 7, 5, 6, 1, 4]

                5
           2         1
        3     7   6     4

첫 단과 두번째 단의 idx 차이가 2**1승 -> 2**(k-2)
두번째 단과 세번째 단의 idx 차이가 2**0승 -> 2**(k-3)
'''