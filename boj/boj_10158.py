W, H = map(int, input().split())
x, y = map(int, input().split())

t = int(input())

dx = (x+t) // W
dy = (y+t) // H

if dx % 2:
    x = W - ((x+t) % W)
else:
    x = (x+t) % W

if dy % 2:
    y = H - ((y+t) % H)
else:
    y = (y+t) % H
print(x, y)
