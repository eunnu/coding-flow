x, y = map(int, input().split())
N = int(input())
store = []
for _ in range(N):
    store.append(list(map(int, input().split())))

direction, idx = map(int, input().split())

ans = 0
for i in range(N):
    if direction == 1:
        if store[i][0] == 1:
            tmp = idx - store[i][1]
            if tmp < 0:
                ans = ans - tmp
            else:
                ans += tmp
        elif store[i][0] == 2:
            tmp = idx + y + store[i][1]
            if tmp > 2*x + 2*y - tmp:
                ans += 2*x + 2*y - tmp
            else:
                ans += tmp
        elif store[i][0] == 3:
            ans += idx + store[i][1]
        else:
            ans += x-idx + store[i][1]

    elif direction == 2:
        if store[i][0] == 2:
            tmp = idx - store[i][1]
            if tmp < 0:
                ans = ans - tmp
            else:
                ans += tmp
        elif store[i][0] == 1:
            tmp = idx + y + store[i][1]
            if tmp > 2*x + 2*y - tmp:
                ans += 2*x + 2*y - tmp
            else:
                ans += tmp
        elif store[i][0] == 3:
            ans += idx + y - store[i][1]
        else:
            ans += x - idx + y - store[i][1]

    elif direction == 3:
        if store[i][0] == 3:
            tmp = idx - store[i][1]
            if tmp < 0:
                ans = ans - tmp
            else:
                ans += tmp
        elif store[i][0] == 4:
            tmp = idx + x + store[i][1]
            if tmp > 2 * x + 2 * y - tmp:
                ans += 2 * x + 2 * y - tmp
            else:
                ans += tmp
        elif store[i][0] == 1:
            ans += idx + store[i][1]
        else:
            ans += y - idx + store[i][1]

    else:
        if store[i][0] == 4:
            tmp = idx - store[i][1]
            if tmp < 0:
                ans = ans - tmp
            else:
                ans += tmp
        elif store[i][0] == 3:
            tmp = idx + x + store[i][1]
            if tmp > 2 * x + 2 * y - tmp:
                ans += 2 * x + 2 * y - tmp
            else:
                ans += tmp
        elif store[i][0] == 1:
            ans += idx + x - store[i][1]
        else:
            ans += y - idx + x - store[i][1]


print(ans)