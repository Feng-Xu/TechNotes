# 练习一 异常
# 在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
# 通过Python程序产生IndexError，并用try捕获异常处理
try:
    a + 1
    str1 = 'asd'
    print(str1[3])
    d = {'a':1}
    print(d[c])
except NameError as e1:
    print(e1)
except IndexError as e:
    print(e)
except KeyError as e2:
    print(e2)

try:
    a = 'qwe'
    print(a[3])
except IndexError as e:
    print(e)
finally:
    print('怎么着都执行')