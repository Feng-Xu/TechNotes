import threading
import time


def myThread(arg1, arg2):
    print(threading.current_thread().getName() + ' start ' + str(time.time()))
    print('%s %s' % (arg1, arg2))
    time.sleep(1)
    print(threading.current_thread().getName() + ' stop ' + str(time.time()))


for i in range(1, 6, 1):
    pass
    # a1 = myThread(i, i+1)
    # a1 = threading.Thread(target=myThread, args=[i, i + 1])
    # a1.start()

    # a1.join()

# print(threading.current_thread().getName() + str(time.time()) + ' end')


# Thread 类

# def __init__(self, group=None, target=None, name=None,
#                args=(), kwargs=None, *, daemon=None):
# target:  指定线程由run()方法调用的可调用对象，默认为None，意味着不调用
# name：指定该线程的名称，在默认情况下，创建一个唯一的名字
# args： target调用的实参，元组格式。默认为()，不传参
# daemon： 默认为Falsa，表示父线程在运行结束时需要等待子线程结束后才能结束程序。为True则表示父线程在运行结束时，子线程是否有任务未完成都会跟随父进程结束，结束程序。
print('===============')


# 线程启动
# 线程执行的目标函数
def worker(arg):
    print("I am working {}".format(arg))
    print('Finished')


# 线程对象
t = threading.Thread(target=worker, args=(threading.current_thread(),), name='FirstThread')
# 启动线程
t.start()

print('==================')


# 线程传参
# 线程的传参和函数传参没有区别，只需要注意传入的必须为元祖格式。
def add(x, y):
    print(x + y)


t1 = threading.Thread(target=add, args=(4, 5))
t1.start()

print('****end****')

print('==================')
# 线程的退出
# 如果线程中任务是无限循环语句，那这个线程将无法自动停止。
# Python线程退出条件有以下几种：
# 1、线程内的函数语句执行完毕，线程自动结束
# 2、线程内的函数抛出未处理的异常

import time


def worker1(args):
    while True:
        time.sleep(1)
        print("I'm working {}".format(args))
    print('Finished')


# 线程启动后，将一直循环下去，线程不会自动退出
# args中相当于主程序调用，线程名字和子线程名字一样
# t2 = threading.Thread(target=worker1, args=(threading.current_thread(),))
# t2.start()
# print('======end=======')

########################
print('==============')


def worker2(args):
    count = 0
    while True:
        if count > 5:
            raise RuntimeError(count)
        time.sleep(1)
        print("I'm working {}".format(args))
        count += 1
    print('Finished')


# 这个例子中，演示触发了异常自动退出程序，但是先打印的是主程序的“======end=====”
# 是因为主程序中，主线程启动一个线程后，不会等待子线程执行完毕，就执行了后续语句，在执行完主线程语句后，发现还有
# 子线程没有结束，于是等待子线程执行完毕，子线程在执行过程中触发了异常，最终子线程结束，主线程也随之结束。
# t3 = threading.Thread(target=worker2, args=(threading.current_thread(),))
# t3.start()
print('======end=======')


# 运行结果
# ======end=======
# I'm working <_MainThread(MainThread, stopped 4463846848)>
# I'm working <_MainThread(MainThread, stopped 4463846848)>
# I'm working <_MainThread(MainThread, stopped 4463846848)>
# I'm working <_MainThread(MainThread, stopped 4463846848)>
# I'm working <_MainThread(MainThread, stopped 4463846848)>
# Exception in thread Thread-2:
# Traceback (most recent call last):
#   File "/Users/xufeng/.pyenv/versions/3.7.0/lib/python3.7/threading.py", line 917, in _bootstrap_inner
#     self.run()
#   File "/Users/xufeng/.pyenv/versions/3.7.0/lib/python3.7/threading.py", line 865, in run
#     self._target(*self._args, **self._kwargs)
#   File "/Users/xufeng/Documents/workspace/python/geektime/classCode/thread_test.py", line 90, in worker2
#     raise RuntimeError(count)
# RuntimeError: 6
#
# I'm working <_MainThread(MainThread, stopped 4463846848)>


# threading属性
# threading.current_thread()  # 返回当前线程队形
# threading.main_thread()     # 返回主线程对象
# threading.active_count()    # 返回处于Active状态的线程个数
# threading.enumerate()       # 返回所有存活的线程的列表，不包括已经终止的线程和未启动的线程
# threading.get_ident()       # 返回当前线程的ID，非0整数

def show_thread_info():
    print("current thread = {}".format(threading.current_thread()))
    print("main thread = {}".format(threading.main_thread()))
    print("active thread count = {}".format(threading.active_count()))
    print("active thread list = {}".format(threading.enumerate()))
    print("thread id = {}".format(threading.get_ident()))
    print("***********************")


def add_v2(x, y):
    time.sleep(1)
    show_thread_info()
    print(x + y)


# show_thread_info()
# time.sleep(1)
#
# t4 = threading.Thread(target=add_v2, args=(3, 4))
# t4.start()
print('~~~~end~~~~~~')


# 运行结果
# current thread = <_MainThread(MainThread, started 4553389504)>
# main thread = <_MainThread(MainThread, started 4553389504)>
# active thread count = 1
# active thread list = [<_MainThread(MainThread, started 4553389504)>]
# thread id = 4553389504
# ***********************
# ~~~~end~~~~~~
# current thread = <Thread(Thread-2, started 123145330368512)>
# main thread = <_MainThread(MainThread, stopped 4553389504)>
# active thread count = 2
# active thread list = [<_MainThread(MainThread, stopped 4553389504)>, <Thread(Thread-2, started 123145330368512)>]
# thread id = 123145330368512
# ***********************
# 7

#########################
