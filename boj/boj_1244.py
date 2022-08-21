'''
아이디어 : 입력을 받는 대로 여학생, 남학생 함수로 이동하여 스위치를 전환해주었음
남학생의 경우 1씩 증가하는 자연수를 곱해준 값의 -1 을 전환
여학생의 경우 입력받은 숫자의 -1 을 기준으로 -1과 +1의 값이 동일하면 바꿔주고 아니면 함수를 종료 시킴
출력할 때, True = 1, False = 0으로 바꾸어 출력해 주었고 각 줄 끝에 띄어쓰기가 존재하는 경우 틀리므로 이 점 유의할 것!!
'''


def man(num):  # 남학생인 경우
    m_idx = 1
    while m_idx <= N//num:
        switch[num*m_idx-1] = not switch[num*m_idx - 1]
        m_idx += 1


def woman(num):  # 여학생인 경우
    idx = 1
    flag = True
    switch[num] = not switch[num]  # 입력 받은 인덱스의 값을 전환
    if 0 <= num-idx and num + idx < N:  # 길이가 3 이상인 경우만 가능함
        while flag:
            if switch[num-idx] == switch[num+idx]:           # 만약 대칭이라면
                switch[num - idx] = not switch[num - idx]    # 그 두개의 스위치 값을 전환시켜 줌
                switch[num + idx] = not switch[num + idx]
                idx += 1
                if num - idx < 0 or num + idx >= N:
                    flag = False
            else:
                flag = False


N = int(input())
switch = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, number = map(int, input().split())
    if gender == 1:
        man(number)
    else:
        woman(number-1)

cnt = 0
for i in range(N):
    if switch[i]:
        switch[i] = 1
    else:
        switch[i] = 0
    if cnt == 19 or i == N-1:
        print(switch[i])
        cnt = 0
    elif cnt < 19:
        print(switch[i], end=' ')
        cnt += 1
