T = int(input())

for tc in range(1, T+1):
    n = input()
    num = list(map(str, input().split()))

    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt_num = [0] * 10

    for i in range(10):
        for j in range(len(num)):
            if number[i] == num[j]:
                cnt_num[i] += 1

    print(f"#{tc}")
    for i in range(10):
        for _ in range(cnt_num[i]):
            print(number[i], end=" ")

    print()
