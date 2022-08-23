def comb(idx):
    temp = []
    for i in range(10):
        if visit[i]:
            temp.append(arr[i])
    if sum(temp) == 10:
        ans.append(temp)

    if idx == 10:
        return

    visit[idx] = 0
    comb(idx+1)
    visit[idx] = 1
    comb(idx+1)


arr = [i for i in range(1, 11)]
visit = [0]*10
ans = []
comb(0)
print(ans)