while True:
    N = input()
    if N == "0":
        break

    mid = len(N) // 2
    if len(N) % 2:
        for i in range(mid):
            if N[i] != N[-1 - i]:
                print("no")
                break
        else:
            print("yes")
    else:
        for i in range(mid+1):
            if N[i] != N[-1 - i]:
                print("no")
                break
        else:
            print("yes")