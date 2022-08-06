T = int(input())

for tc in range(1, T + 1):                                  
    N = int(input())

    def check():                                # 
        global res                              # 갯수를 저장해 줄 res 변수 global 선언
        temp = ''
        temp_num = 0                            # 알파벳의 길이가 26개인지를 확인 해줄 변수
        for i in range(len(visited)):           # visited 리스트의 길이 만큼 반복해 줌
            if visited[i]:                      # 방문한 idx 인 경우
                temp += word[i]                 # 해당 idx 값을 입력받은 word 리스트에서 가져와 temp에 더해줌
                temp_num = len(set(temp))       # 반복되는 알파벳을 지우면서 해당 길이를 저장
            if temp_num == 26:                  # 알파벳의 길이가 26 이면 res를 하나 더해주고 종료
                res += 1
                break

    def combi(idx, cnt, num):                   # 조합을 만들어 줄 함수(현재 위치, 현재 갯수, 만드려는 조합의 갯수)
        if num == cnt:                          # 현재 갯수와 만드려는 조합의 수가 일치하면
            check()                             # 그 조합이 세트의 기준을 확인하는 함수로 이동
            return
        for i in range(idx, len(visited)):      # 조합 만들어 주는 반복문
            if visited[i]: continue             # 현재 방문했던 idx이면 continue
            visited[i] = 1                      # 아니라면 1을 입력해준다

            combi(i, cnt+1, num)                # 그 상태로 재귀를 돌아줌(현재 위치, 현재 갯수, 만족해야 하는 갯수)
            visited[i] = 0                      # return이 되면 해당 visited idx를 0으로 바꿔줌

    word = []
    for _ in range(N):
        temp = input()
        word.append(temp)

    combi_li = []                               # 모든 조합을 넣어줄 리스트
    visited = [0]*N                             # 방문값을 저장해줄 리스트를 선언
    global res
    res = 0 
    
    for i in range(1,N+1):                      # 단어의 조합이 1개 부터 단어의 갯수만큼 만들어 져야 하기 때문에 1부터 N까지 반복
        combi(0, 0, i)                          # start 0, 초기 갯수 0, 만족해야 하는 갯수 1부터 N까지

    print(f'#{tc} {res}')       
