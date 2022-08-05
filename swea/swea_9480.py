import itertools
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    word = []
    for _ in range(N):
        temp = input()
        word.append(temp)

    # def combi(arr, r, combi_li):
    #     arr = sorted(arr)
    #     li = []
    #     def generate(chosen):
    #         if len(chosen) == r:
    #             li.append(chosen)
    #             combi_li.append(li)
    #             return 

    #         start = arr.index(chosen[-1]) + 1 if chosen else 0
    #         for nxt in range(start, len(arr)):
    #             chosen.append(arr[nxt])
    #             generate(chosen)
    #             chosen.pop()
    #     generate(li)

    combi_li = [] # 모든 조합을 넣어줄 리스트
    for i in range(1,N+1):
        combi_li += list(itertools.combinations(word, i))

    res = 0 
    
    for i in combi_li:
        temp =  ''
        for j in i:
            temp += j
            # 조합 단어를 모두 더해 중복되는 알파벳을 전부 지움
            temp_num = len(set(temp))
            if temp_num == 26: #길이가 알파벳이면
                res += 1 #결과를 더해준다.
                break        
    print(f'#{tc} {res}')
