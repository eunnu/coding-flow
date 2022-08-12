delet = 'CAMBRIDGE'

letter = input()
ans = ''
for i in letter:
    if i in delet:
        continue
    else:
        ans += i

print(ans)