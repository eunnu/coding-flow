'''
i == 0 : 학생수가 주어지기 때문에 stu[0] = 1
if 뽑은 번호가 n이면 현재 위치를 원하는 위치에 넣음

ex)
N = 5
0 1 1 3 2
초기 세팅 : stu = [1]
'''

# 걸린 시간 :

N = int(input())
num = list(map(int, input().split()))

stu = [1]

for i in range(2, N + 1):
    stu.insert(len(stu)-num[i - 1], i)

    # 번호를 넣어 주기 위해 2부터 N까지 반복
    # 0 1 1 3 2
    # [1]           -> len(stu) = 1 / num[2-1] = 1 / stu[0] = 2   -> stu = [2, 1]
    # [2, 1]        -> len(stu) = 2 / num[3-1] = 1 / stu[1] = 3   -> stu = [2, 3, 1]
    # [2, 3, 1]     -> len(stu) = 3 / num[4-1] = 3 / stu[0] = 4   -> stu = [4, 2, 3, 1]
    # [4, 2, 3, 1]  -> len(stu) = 4 / num[5-1] = 2 / stu[2] = 5   -> stu = [4, 2, 5, 3, 1]

for i in stu:
    print(i, end=" ")




