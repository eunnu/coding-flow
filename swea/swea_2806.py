def queen(depth):
    global res
    if depth == N:
        res += 1
        return
    else:
        temp = []
        if visit:
            for i in range(depth):
                temp.append(visit[i])
                temp.append(visit[i] - depth + i)
                temp.append(visit[i] + depth - i)

        for i in range(N):
            if i not in temp:
                visit.append(i)
                queen(depth+1)
                visit.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visit = []
    res = 0
    queen(0)
    print(f"#{tc} {res}")