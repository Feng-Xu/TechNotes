import pysnooper

# 可变长参数
# other内容为一个元组，里面放着其他参数
def func_len(first, *other):
    #print(len(first))
    print(len(other))
    print(other)
    print(other[0])
    print(other[1])
    print(type(other))


func_len(123, 12, 24)

# 函数作用域
var1 = 123

# global可以将变量设置为全局变量
def print_var():
    global var1
    var1 = 456
    print(var1)

print("函数中的值：", end='')
print_var()
print("函数外的值：%d" % var1)


print("======================")
list1 = [1,2,3]
print(list1)
# 迭代器
it = iter(list1)
print(it)
# next()逐步取出迭代器中的值
print(next(it))
print(next(it))
print(next(it))
#print(next(it))



print("======================")
#  yield的主要用途是需要一个数据时，才产生一个，而不是把数据线一次性存入内存；相对于把数据提前定义成列表来使用，要极为节省系统资源。
# 一般访问生成器要使用next方法，也可以使用list方法一次性讲将所有值读取出来，但是一次性读取出来就和列表一样了，失去自身的优势。
# 带yield的函数我们称为迭代器，这种函数返回的是一个固定的对象，叫迭代器对象，它和return的最大区别是，如果你需要返回无限序列，
# return会产生一个巨大的列表，很明显存在内存限制问题。所以引入了yield返回一个固定长度的值。
def frange(start, stop, step):
    while start < stop:
        yield start
        start = start + step

for i in frange(10, 15, 0.35):
    print(i)


# Fibonacci
#@pysnooper.snoop()
def feb(max):
    a = 0
    b = 1
    n = 0
    while n < max:
        print(b)
        a, b = b, (a + b)
        n = n + 1
feb(5)