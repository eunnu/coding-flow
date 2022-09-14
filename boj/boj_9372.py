'''
이 문제는 왜 여기 있는지 모르겠는데...
의도는 최소신장트리인거 같은데 그러려면 이렇게 내면 안되는거 아닌가...
이렇게 되면 당연히 나라 - 1 이 아닌가..
이렇게 푸는거 아닌가..?
'''


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        P, Q = map(int, input().split())

    print(N - 1)