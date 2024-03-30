import sys
A, B, V = map(int, sys.stdin.readline().split(" "))
print((V - A)//(A - B) + 1 + int(bool((V - A) % (A - B))))
