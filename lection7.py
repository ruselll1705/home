# s, i = 's', 0
# try:
#     s=int(s)/i
# except ValueError as e:
#     print(e)
# except ZeroDivisionError:
#     print('Zero division error')
# try:
#     1/0
# except Exception as e:
#     print(e)
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(unknov_var)
# finally:
#     print('This is executed last')
# f = open("test4.txt")
# f1=f.read()
# print(f1)
# try:
#     print(int(f1))
# except ValueError as e:
#     print(e)
# else:
#     print('Oshibok net')
# finally:
#     f.close()
#     print('zakritie')
# print(10)
# raise ValueError
# print('am i')
# name = '3elena'
# if name[0].isnumeric():
#     raise NameError('invalid name')
# while True:
#     x = input('vvedite chislo ')
#     try:
#         print(float(x))
#     except ValueError as e:
#         pass
#     else:
#         break

# function

# def sd(x):
#     x[0],x[-1]=x[-1],x[0]
#     return(x)
# print(sd([1,2,'res']))
# def f(a, b,c):
#     return a+b+c
# print(f(3,5))
def min_2(*s):
    if len(s)==1:
        return 'peredaite dva znacheniya'
    else:
        s=list(s)
        s.sort()
    #b=sorted(s)
        return s[1]
print(min_2(4,9,6,7))
print(min_2(2))