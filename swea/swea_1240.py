# 비밀번호가 존재하는 줄을 찾아서
# 처음부터 56번까지 암호를 확인한다.
# 중간에라도 암호가 아닌 경우 반환한다.
def sol(n_idx):
    global idx
    tmp = ""
    cnt, num = 0, 0
    for j in range(n_idx, n_idx + 56):
        if li[idx][j - 1] == li[idx][j]:
            cnt += 1
        else:
            if num != 6:
                tmp += str(cnt+1)
                cnt = 0
        num += 1
        if num == 7:
            tmp += str(cnt + 1)
            cnt, num = 0, 0

        if len(tmp) == 4:
            if tmp in code:
                for k in range(10):
                    if code[k] == tmp:
                        pw.append(k)

            else:
                return
            tmp = ""


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [input() for _ in range(N)]

    code = ["3211", "2221", "2122", "1411", "1132", "1231", "1114", "1312", "1213", "3112"]

    idx = 0
    for i in range(N):
        if "1" in li[i]:
            idx = i
            break

    pw = []
    for i in range(M - 56):
        pw = []
        sol(i)
        if len(pw) == 8:
            break

    a = 0
    for i in range(0, 8, 2):
        a += pw[i]

    b = sum(pw) - a
    if (3*a + b) % 10:
        print(f"#{tc} {0}")
    else:
        print(f"#{tc} {sum(pw)}")