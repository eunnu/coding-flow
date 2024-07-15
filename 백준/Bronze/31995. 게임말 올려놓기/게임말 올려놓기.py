from sys import stdin

inp = stdin.readline
N = int(inp())
M = int(inp())

print((N-1)*(M-1)*2 if (N-1)*(M-1)*2 > 0 else 0)