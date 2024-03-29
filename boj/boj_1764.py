import sys

N, M = map(int, input().split(" "))
name_li = set()
db_li = set()
result = []
for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    name_li.add(temp)

for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    db_li.add(temp)

name_li = list(set.intersection(name_li, db_li))
name_li.sort()
print(len(name_li))
for i in name_li:
    print(i)