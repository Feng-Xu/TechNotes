# Python2.2之前定义了三个作用域，分别是：
# local作用域，对应local命名空间，由函数定义的。
# global作用域，对应的global命名空间，一个模块最外层定义的一个作用域。
# builtin作用域，对应builtin命名空间，python内部定义的最顶层的作用域，在这个作用域里面定义了各种内建函数：open、range、xrange、list等等。
# Python2.2之前，作用域规则叫做LEB规则，变量（名字）的引用按照local作用域、global作用域、builtin作用域的顺序来查找。

a = 1
def foo():
    a = 2
    def bar():
        print(a)
    return bar

func = foo()
func()

# Python2.2之后
# 引入嵌套函数，嵌套函数为python提供了闭包实现。
# locals 是函数内的名字空间，包括局部变量和形参
# enclosing 外部嵌套函数的名字空间（闭包中常见）
# globals 全局变量，函数定义所在模块的名字空间
# builtins 内置模块的名字空间
# 函数bar和a=2捆包在一起组成一个闭包，但调用func的时候（其实就是调用bar）查找名字a的顺序是LEGB规则，
# 这里的E就是enclosing的缩写，代表的“直接外围作用域”这个概念。查找a时，在bar对应的local作用域中没有时，然后在它外围的作用域中查找a。
# LEGB规定了查找一个名称的顺序为：local-->enclosing-->global-->builtin。

# 修改global变量的话，得在函数内部使用global声明改变量
a1 = 0
def foo_global():
    global a1
    a1 = 1
    print('local:', a1)

func_global = foo_global()
print('global:', a1)

# 修改enclosing变量，得使用nonlocal关键字来修改
a2 = 0
def foo_enclosing():
    a2 = 1
    def bar():
        nonlocal a2
        a2 = 2
        print('in_enclosing:', a2)
    # 不注释的话，相当于执行了bar函数，声明了a2是nonlocal类型，作用域在上一层，in & out enclosing都是2
    # 注释的话，调用foo_enclosing()函数，相当于里面bar()函数没执行，所以out enclosing为1，当执行了func_enclosing()，里面bar()函数会执行，in & out enclosing为2
    #bar()
    print('out_enclosing:', a2)
    return bar

func_enclosing = foo_enclosing()
func_enclosing()

# nonlocal不能代替global域
# 在多重嵌套中，nonlocal只会上溯一层； 而如果上一层没有，则会继续上溯。
# 最终会上溯到global域，但是到global域就会报错。
i = 0

def a():
    i = 1

    def b():
        nonlocal i
        i = 2

    b()
    print(i)

a()



#cnt = 1
def counter():
    cnt = 1
    def add_one():
        #nonlocal cnt
        a = cnt + 1
        return a
    return add_one

num = counter()
print(type(num))
print(num())
print(num())

# def a_line(a, b):
#     def arg_y(x):
#         return a * x + b
#     return arg_y

# lamda定义闭包
def a_line(a, b):
    return lambda x: a * x + b


# a = 3, b = 5的直线
line1 = a_line(3,5)
print(line1(10))

# a = 5, b = 10的直线
line2 = a_line(5, 10)
print(line2(10))