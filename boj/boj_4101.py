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

# a, b = map(int, input().split())
# c = int(input())
# if((b+c) >= 60):
#     d = (b + c) // 60
#     if((a+d) >= 24):
#         e = (a+d)//24
#         print((a+d)-24*e, (b+c)-(60*d))
#     else :
#         print(a + d, (b+c)-(60*d))
# else :
#     print(a, b+c)

# year = int(input())
# if(not(year%4) and (year%100) or not(year%400)):
#     print('윤년입니다')
# else :
#     print('윤년이 아닙니다')

# a, b , c= map(int, input().split())
# d = int(input())
# if((d+c) >= 60):
#     e = (d + c) // 60
#     if((b+e) >= 60):
#         f = (b+e)//60
#         if((a+f)>=24):
#             g = (a+f)//24
#             print((a+f)-24*g, (b+e)-(60*f), (c+d)-(60*e))
#         else :
#             print(a + f, (b+e)-(60*f), (c+d)-(60*e))
#     else :
#         print(a, b+e, (c+d)-(60*e))
# else :
#     print(a, b, c+d)

# a, i = map(int, input().split())
# n =  a * (i-1) +1
# print(n)

# t = int(input())
# while(t > 0):
#     s = list(map(str, input().split(' ')))  
#     n = float(s[0])
#     res = 0
#     res += n
#     i = 1
#     for i in range(len(s)):
#         if s[i] == "@":
#             res = res * 3
#         elif s[i] == "%":
#             res = res + 5
#         elif s[i] == "#":
#             res = res - 7
#     print('%0.2f' % res)
#     t = t - 1
