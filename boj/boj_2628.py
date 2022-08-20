'''
아이디어
입력 받은 데이터를 세로와 가로로 나누어서 값을 오름차순으로 정렬하고
요소의 차이를 비교하여 가장 긴 길이 끼리 곱해주었음
ex) 10 8 // 0 2, 0 3, 1 4
가로 리스트 : 0, 2, 3, 8
세로 리스트 : 0, 4, 10
가로 가장 긴 길이 : 5
세로 가장 긴 길이 : 6
5 * 6 = 30
'''
W, H = map(int, input().split())

N = int(input())
cut_w = [0]  # 시작 점
cut_h = [0]  # 시작 점
for i in range(N):
    A, B = map(int, input().split())
    if A:
        cut_w.append(B)  # 세로 선
    else:
        cut_h.append(B)  # 가로 선

cut_h.append(H)  # 정점을 넣어줌
cut_w.append(W)  # 정점을 넣어줌

cut_w.sort()
cut_h.sort()

long_height = 0
for i in range(len(cut_h) - 1):
    if cut_h[i+1] - cut_h[i] > long_height:
        long_height = cut_h[i+1] - cut_h[i]

long_width = 0
for i in range(len(cut_w) - 1):
    if cut_w[i+1] - cut_w[i] > long_width:
        long_width = cut_w[i+1] - cut_w[i]

print(long_width*long_height)