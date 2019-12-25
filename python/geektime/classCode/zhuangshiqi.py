# 装饰器本质上是一个 Python 函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下增加额外功能，装饰器的返回值也是一个函数/类对象。
# 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景，装饰器是解决这类问题的绝佳设计。
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码到装饰器中并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

# 装饰器类似闭包，装饰器传入的是函数或者类对象，闭包传入参数是变量。

import logging
import time


def use_logging(func):
    def wrapper():
        logging.warning('%s is running' % func.__name__)
        return func()
        # func()

    return wrapper


# 装饰器的语法糖
@use_logging
def foo():
    print('i am foo')


# foo1 = use_logging(foo)
foo()


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        # return end_time - start_time
        print(end_time - start_time)

    return wrapper


@timmer
def i_can_sleep():
    time.sleep(3)


# func1 = timmer(i_can_sleep)
# func1()
i_can_sleep()

print("带参数的装饰器")


def new_tips(func_wai):
    def tips(func):
        def wrapper(*args):
            print(func_wai)
            print('start %s' % func.__name__)
            func(*args)
            print('end %s' % func.__name__)

        return wrapper

    return tips


@new_tips('add_module')
def add(a, b):
    print(a + b)


add(10, 10)
