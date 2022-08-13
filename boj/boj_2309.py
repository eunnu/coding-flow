nine = []
# 9명 난쟁이 키 리스트
for _ in range(9):
    nine.append(int(input()))

seven = []
# 7명 난쟁이 키 리스트

flag = False
# 반복문 탈출

for i in range(9):
    for j in range(9):
        if i == j:
            # 방문한 곳은 더 방문 안하겠다는 뜻
            continue
        for k in range(9):
            if k != j and k != i:
                # 방문한 곳은 더 방문 안한다는 뜻
                seven.append(nine[k])
                # 방문 한 적 없으면 해당 값을 넣어줌
                if len(seven) == 7 and sum(seven) == 100:
                    flag = True
                    break
                    # 길이가 7이면서 합이 100 이면 flag 를 True
                elif len(seven) == 7 and sum(seven) != 100:
                    seven.clear()
                    continue
                    # 길이가 7인데 합이 100이 안되면 리스트를 비워줌
        if flag:
            break
    if flag:
        break

seven.sort()
for i in seven:
    print(i)