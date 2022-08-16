import sys
sys.stdin = open("input.txt", "r")

T = 10

for _ in range(T):
    tc = int(input())

    ans = 0
    arr = []
    for _ in range(100):
        arr.append(list(input()))           # str 은 알아서 나눠서 넣어진다. 숫자와 다름

    for i in range(100):                    # 100줄 반복
        for j in range(99):                 # 99까지만 반복
            for k in range(j+1, 100):       # 문자열의 크기가 최대 100까지
                temp = arr[i][j:k+1]        # 임시 변수에 문자열 크기만큼 넣어주고
                if temp == temp[::-1]:      # 뒤집어도 같은데
                    if ans < len(temp):     # 길이가 최대 보다 길다면
                        ans = len(temp)     # 최대 길이 업데이트

    brr = list(zip(*arr))
    # 가로 세로 전치

    for i in range(100):
        for j in range(99):
            for k in range(j+1, 100):
                temp = brr[i][j:k+1]
                if temp == temp[::-1]:
                    if ans < len(temp):
                        ans = len(temp)

    print(f"#{tc} {ans}")