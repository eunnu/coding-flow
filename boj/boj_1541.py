S = input()
M = S.split("-")
re = sum(map(int, M[0].split("+")))
for i in M[1:]:
    re -= sum(map(int, i.split("+")))
print(re)