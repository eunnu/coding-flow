s = 'one2three4'
num_e = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ans = ''

for i in range(len(s)):
    if s[i] in num:
        ans += s[i]
        continue
    for j in range(6):
        n = ''
        n += s[i:i+j]
        if n in num_e:
            for k in range(10):
                if n == num_e[k]:
                    ans += str(k)
            break
print(int(ans))