'''
아이디어 : 북, 남 을 가리키는 길이와, 동, 서를 가리키는 길이를 각각 저장
두 리스트를 정렬하면 가장 긴 값들이 전체 가로와 세로의 길이가 됨
전체 방향과 길이를 넣은 리스트를 2배 길이로 만들어 방향전환이 동일한 구간의 길이를 곱해서 작은 구역의 넓이를 구해줌
ex) 1 4 1 4 -> 가운데 1과 4의 길이를 곱해줌
'''


N = int(input())
h = []
w = []
arr = []
for i in range(6):
    arr.append(list(map(int, input().split())))
    if arr[i][0] < 3:
        w.append(arr[i][1])
    else:
        h.append(arr[i][1])

w.sort()
h. sort()
small = 0

for i in range(10):
    arr.append(arr[i])
    # 뒤에 넣어주는 이유는 가운데에 존재하는게 아닌 양 끝에 존재할 수 있기 때문
    # ex) 1 4 2 3 1 3 -> 1 3 1 3 이 양 끝에 존재하기 때문에 이를 확인하기 위해 구간을 넓혀줌
    if arr[i][0] == arr[i+2][0] and arr[i+1][0] == arr[i+3][0]:
        small = arr[i+1][1] * arr[i+2][1]

area = (w[-1]*h[-1] - small) * N
print(area)
