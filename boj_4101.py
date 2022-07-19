# while (1) :
#     a , b = map(int, input().split())
#     if (a == b == 0) : break
#     print('Yes' if a > b else 'No')

# a , b = map(int, input().split())
# print(b*2 - a)

# a , b = map(int, input().split())
# print(a*b - 1)

# from datetime import datetime
# print(datetime.today().strftime('%Y-%m-%d'))

a, b = map(int, input().split())
c = int(input())
if((b+c) >= 60):
    d = (b + c) // 60
    if((a+d) >= 24):
        e = (a+d)//24
        print((a+d)-24*e, (b+c)-(60*d))
    else :
        print(a + d, (b+c)-(60*d))
else :
    print(a, b+c)

