# 시간 초과를 해결하려면 비둘기집 원리를 알아야 함
# mbti는 16가지, 17사람이면 무조건 2명은 겹침 그렇기 때문에 33명이면 무조건 3명이 겹침
from sys import stdin
from itertools import combinations

for _ in range(int(stdin.readline())):
    num = int(stdin.readline())
    student = list(stdin.readline().split(" "))

    student[-1] = student[-1][:-1]
    if num > 32:
        print(0)
    else:
        temp = combinations(student, 3)
        res = 13
        for i in temp:
            tmp = len(set(i[0]+i[1])) + len(set(i[1] + i[2])) + len(set(i[0] + i[2])) - 12
            if res > tmp:
                res = tmp

        print(res)