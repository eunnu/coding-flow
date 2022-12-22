# 세로로 문자열이 겹치지 않으면 된다.
# 위에서 아래로 내려가면 시간초과가 뜸
# 가장 아랫 줄에 같은 알파벳이 없으면 겹치는 문자열이 없음 -> 해당 열만 확인
# 같은 알파벳이 존재하면 세로로 확인함
# 맨 위 행은 확인 할 필요가 없음
def sol():
    tmp = [''] * c

    for idx in range(r-1, -1, -1):
        string = set()
        for jdx in range(c):
            tmp[jdx] = li[idx][jdx] + tmp[jdx]
            string.add(tmp[jdx])
        if c == len(string):        # 맞은 코드 => 중복이 안되려면 문자열 개수와 c의 개수가 같아야 한다.
            return idx
            # 틀린 코드 => 중복이 발생하면 해당 위치에서 -1 을 뺀 값을 해주었음
            # 틀린 이유 : 메모리 초과/시간 초과 => 어디서 부터 중복이 된건지 모르기 때문에 전체를 넣어주다 보니 메모리 초과가 발생한 듯
            # 메모리 초과를 해결하기 위해 각 행마다 set를 선언해 줌.. 과연 이것 때문에 통과가 된건지는 모르겠음..
            # if tmp not in string:
            #     string.add(tmp)
            # else:
            #     res = min(res, jdx-1)

r, c = map(int, input().split())
li = [input() for _ in range(r)]
result = 0
st = []
st.extend(li[r-1])
b = list(set(st))
if len(b) == len(st):
    result = r-1
else:
    result = sol()
print(result)

