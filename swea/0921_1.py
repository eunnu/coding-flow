def Selecsort(A, s):
    n = len(A)
    if s == n-1:
        return
    mini = s
    for idx in range(s, n):
        if A[mini] > A[idx]:
            mini = idx
    A[s], A[mini] = A[mini], A[s]
    SSort(A, s+1)


A = [2, 4, 6, 1, 9, 8, 7, 0]
SSort(A, 0)
print(A)