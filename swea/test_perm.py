a = [1, 2, 3]
b = []

def perm(idx):
    if idx == 3:
        b.append(list(k for k in a))
    else:
        for i in range(idx, 3):
            a[idx], a[i] = a[i], a[idx]
            print(i, idx, a)
            perm(idx + 1)
            a[idx], a[i] = a[i], a[idx]
perm(0)
print(b)

