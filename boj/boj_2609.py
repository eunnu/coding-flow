A, B = map(int, input().split(" "))

OA, OB = max(A, B), min(A, B)

while A != 0 and B != 0:
    if A < B:
        A, B = B, A

    temp = A % B
    A, B = B, temp

resultA, resultB = A, 0
A, B = OA, OB
i, j = 1, 1
while True:
    flag = False
    while A * i >= B * j:
        if A * i == B * j:
            flag = True
            break
        j = j + 1
    if flag:
        break
    i = i + 1

resultB = OA * i
print(resultA)
print(resultB)