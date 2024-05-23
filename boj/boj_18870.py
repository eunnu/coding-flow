import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split(" ")))
num_sort = sorted(list(set(num)))
num_dict = {}
for i in range(len(num_sort)):
    if num_sort[i] not in num_dict:
        num_dict[num_sort[i]] = i

for i in range(N):
    if i == N - 1:
        print(num_dict[num[i]])
    else:
        print(num_dict[num[i]], end=" ")
