# NameError
# i = j

# SyntaxError
# print())

#IndexError
# a = '123'
# print(a[3])

# KeyError
# a = {'a':1, 'b':2}
# # print(a['c'])

# ValueError
# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('input numbers!')

# AttributeError
# a = 123
# try:
#     a.append()
# except AttributeError:
#     print('int has no this append()')

# 可以同时捕获多个异常
# try:
#     i=j
# except (NameError, SyntaxError):
#     print(123)

# 使用Exception捕获所有异常
# try:
#     print(1/0)
# except Exception as e:
#     print('%s' % e)

# 自定义异常
# try:
#     raise NameError('hello xufeng')
# except NameError:
#     print('custom error by xufeng')

# finally 不管怎么都执行
try:
    file1 = open('name.txt')
except Exception as e:
    print(e)
finally:
    file1.close()