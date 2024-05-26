import sys

n, m = map(int, sys.stdin.readline().split(" "))
password = dict()
for _ in range(n):
    temp = sys.stdin.readline().split(" ")
    password[temp[0]] = temp[1][:-1]

ws = list(sys.stdin.readline()[:-1] for _ in range(m))

for i in ws:
    print(password[i])
