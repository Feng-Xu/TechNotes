import threading, time


def add_v3(x, y):
    # _ 你可以当它是一个变量，但一般习惯不用这个变量,只想要循环5次, 而不需要引用计数值,只要循环的过程
    for _ in range(5):
        time.sleep(1)
        print("x+y={}".format(x + y))


class myThread_v3(threading.Thread):
    def start(self):
        print("start----------->")
        # 调用父类的start函数
        super().start()

    def run(self):
        print('run----------->')
        super().run()


# t5 = myThread_v3(target=add_v3, args=(3, 4))
# t5.start()
# t5.run()
# print("==========myThread_v3==========")

# 只调用start()方法的执行结果：(执行结果是先调用start()方法，再运行run()方法。)
# start----------->
# run----------->
# ==========myThread_v3==========
# x+y=7
# x+y=7
# x+y=7
# x+y=7
# x+y=7
#######################
# 只调用run()方法的执行结果：(可以看到是按照代码顺序执行，run函数只是简单的传参，并没有并发)
# run----------->
# x+y=7
# x+y=7
# x+y=7
# x+y=7
# x+y=7
# ==========myThread_v3==========


# threading.Thread中调用顺序：
# start() --> run() --> _target()
# run() --> _target()


def worker():
    count = 1
    while True:
        if count > 6:
            break
        time.sleep(1)
        count += 1
        print("thread name %s, ID: %s" % (threading.current_thread().getName(), threading.current_thread().ident))

# t = threading.Thread(target=worker, name='MyThread-xf')
#t.start()
# t.run()

#print('=====end=====')

# t.start()运行结果：
# =====end=====
# thread name MyThread-xf, ID: 123145348898816
# thread name MyThread-xf, ID: 123145348898816
# thread name MyThread-xf, ID: 123145348898816
# thread name MyThread-xf, ID: 123145348898816
# thread name MyThread-xf, ID: 123145348898816
# thread name MyThread-xf, ID: 123145348898816

# t.run()运行结果：
# 使用的是用run()方法启动线程，它打印的线程名是MainThread，也就是主线程。
# thread name MainThread, ID: 4731839936
# thread name MainThread, ID: 4731839936
# thread name MainThread, ID: 4731839936
# thread name MainThread, ID: 4731839936
# thread name MainThread, ID: 4731839936
# thread name MainThread, ID: 4731839936
# =====end=====


#######################
# 查看多线程的例子
t1 = threading.Thread(target=worker, name='t1')
t2 = threading.Thread(target=worker, name='t2')

# t1.start()
# t2.start()
# print('=====end=====')

# t.start()运行结果：
# start()方法启动了两个新的子线程并交替运行，每个子进程ID也不同。
# =====end=====
# thread name t2, ID: 123145469128704
# thread name t1, ID: 123145463873536
# thread name t2, ID: 123145469128704
# thread name t1, ID: 123145463873536
# thread name t2, ID: 123145469128704
# thread name t1, ID: 123145463873536
# thread name t1, ID: 123145463873536
# thread name t2, ID: 123145469128704
# thread name t1, ID: 123145463873536
# thread name t2, ID: 123145469128704
# thread name t1, ID: 123145463873536
# thread name t2, ID: 123145469128704

t1.run()
t2.run()
print('=====end=====')

# t.start()运行结果：
# 两个子线程都用run()方法启动，但却是先运行t1.run()，运行完之后才按顺序运行t2.run()
# 两个线程都工作在主线程，没有启动新线程，因此，run()方法仅仅是普通函数调用。
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# thread name MainThread, ID: 4493067712
# =====end=====

# 好了，从上面四个小例子，我们可以总结出：
#
# start() 方法是启动一个子线程，线程名就是我们定义的name
# run() 方法并不启动一个新线程，就是在主线程中调用了一个普通函数而已。

默认的run 是没有任何功能的， 你只有重写了run才能通过多线程实现你的功能
threading 模块是实现了多线程的框架，需要多线程做什么事情，要在run里面实现