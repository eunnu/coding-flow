# 세로로 문자열이 겹치지 않으면 된다.
# 위에서 아래로 내려가면 시간초과가 뜸
# 가장 아랫 줄 부터 같은 알파벳이 없으면 겹치는 문자열이 없음 -> 해당 열만 확인
# 같은 알파벳이 존재하면 한 줄 위로 올라감
# 같은 알파벳이 없으면 현재 위치를 저장
# 맨 위 행은 확인 할 필요가 없음
r, c = map(int, input().split())
li = [input() for _ in range(r)]
result = 0
mid = r//2 - 1
for i in range(r-1, 0, -1):
    st = []
    st.extend(li[i])
    b = list(set(st))
    if len(b) == len(st):
        result = max(result, i)
    else:
        result = 0

print(result)

