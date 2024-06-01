from sys import stdin

n = int(stdin.readline())
L = int(stdin.readline())
text = stdin.readline()
# task 1
# P = "IOI" + "OI" * (n-1) 이미 여기에서 시간 복잡도가 증가하게 됨
# res = 0
# tmp = n*2
# for i in range(L - tmp):
#     if text[i:i+tmp+1] == P:
#         res += 1

# task 2
cursor = 0
res = 0
cnt = 0
while cursor < L - 2:
    if text[cursor:cursor + 3] == "IOI":
        cursor += 2
        cnt += 1
        if cnt == n:
            res += 1
            cnt -= 1
    else:
        cursor += 1
        cnt = 0

print(res)
