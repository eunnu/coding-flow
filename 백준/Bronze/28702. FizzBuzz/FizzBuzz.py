from sys import stdin

# 15 단위로 돔
num = [stdin.readline()[:-1] for _ in range(3)]
check = ["Fizz", "Buzz", "FizzBuzz"]
res = 0
sol = 0
for i in range(3):
    if num[i] not in check:
        res = int(num[i]) // 15
        sol = int(num[i]) % 15 + (3-i)
        break

res = res*15 + sol
if not res%3 and not res%5:
    print("FizzBuzz")
elif not res%3 and res%5:
    print("Fizz")
elif res%3 and not res%5:
    print("Buzz")
elif res%3 and res%5:
    print(res)