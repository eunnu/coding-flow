from sys import stdin
S = 0
for _ in range(int(input())):
    ost, *n = stdin.readline().split(" ")
    if n:
        n = int(n[0])
        if ost == "add":
            S |= (1 << n)
        elif ost == "remove":
            S &= ~(1 << n)
        elif ost == "check":
            print(int(bool(S & (1 << n))))
        elif ost == "toggle":
            S ^= (1 << n)
    else:
        if ost == "all\n":
            S = (1 << 21) - 1
        elif ost == "empty\n":
            S = 0



