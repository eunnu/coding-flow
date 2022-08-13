sw = [0]*7
sm = [0]*7
# 여학생, 남학생 1-6학년의 수를 넣어줄 리스트
N, K = map(int, input().split())
# 예시 N, K = 8, 2
for _ in range(N):
    S, C = map(int, input().split())
    if S:
        sm[C] += 1
    # 만약 성별이 1이라면 sm의 학년 인덱스에 +1 을 해줌
    else:
        sw[C] += 1
    # 만약 성별이 0이라면 sw의 학년 인덱스에 +1 을 해줌
'''
1 1
1 1
1 1
1 1
0 1
0 1
0 1
0 1
sw = [0, 4, 0, 0, 0, 0, 0]
sm = [0, 4, 0, 0, 0, 0, 0]
'''
room = 0
# 방의 개수를 넣어줄 변수

for i in range(1, 7):
    if sw[i] > K:  # 성별이 여자이고 학년 수가 K보다 클 경우
        if sw[i] % K:  # 나머지가 존재하는 경우 방이 하나 더 필요
            room += sw[i] // K + 1
        else:  # 방이 꽉 채워지는 경우 방의 개수는 몫
            room += sw[i] // K
    elif sw[i]:  # 인원이 1 ~ K 까지인 경우
        room += 1
    if sm[i] > K:  # 성별이 남자이고 학년 수가 K보다 클 경우
        if sm[i] % K:  # 나머지가 존재하는 경우 방이 하나 더 필요
            room += sm[i] // K + 1
        else:  # 방이 꽉 채워지는 경우 방의 개수는 몫
            room += sm[i] // K
    elif sm[i]:  # 인원이 1 ~ K 까지인 경우
        room += 1

print(room)