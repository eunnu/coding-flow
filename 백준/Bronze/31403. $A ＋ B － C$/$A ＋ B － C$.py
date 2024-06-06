from sys import stdin

num = int(stdin.readline())
st = str(num)

temp = int(stdin.readline())
num += temp
st = st + str(temp)

temp = int(stdin.readline())
print(num - temp)
print(int(st) - temp)