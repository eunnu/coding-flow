from sys import stdin

N = int(stdin.readline())
tree = dict()
for _ in range(N):
    temp = list(stdin.readline().split(" "))
    temp[-1] = temp[-1][:-1]
    tree[temp[0]] = temp[1:]


def pre(d):
    global pre_res, mid_res, back_res
    pre_res += d

    for i in tree[d]:
        if i != ".":
            pre(i)
        if d not in mid_res:
            mid_res += d
    back_res += d
    return


pre_res = ""
mid_res = ""
back_res = ""
pre("A")
print(pre_res)
print(mid_res)
print(back_res)