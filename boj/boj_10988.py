st = input()
n = len(st)
ans = 0
ts = ''
for i in range(n-1, -1, -1):
    ts += st[i]
if ts == st:
    ans = 1
print(ans)