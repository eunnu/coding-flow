T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())


    if (W <= R):
        print('#%d'%test_case, min(Q, P*W))
    else:
        print('#%d'%test_case, min(P*W, (Q + (((W-R)*S)))))