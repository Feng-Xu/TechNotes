# 多线程同时修改全局变量时会出现数据安全问题，线程不安全就是不提供数据访问保护，有可能出现多个线程先后更改数据造成所得到的数据是脏数据。
# 在本例中我们生成2个线程同时修改change()函数里的全局变量balance时，会出现数据不一致问题。

# 先不加锁，运行脚本，当2个线程运行次数达到500000次时，会出现以下结果。
# balance=200
# MainThread 线程结束

# 加上锁后：
# MainThread 线程结束

# 针对线程安全问题，需要使用”互斥锁”，就像数据库里操纵数据一样，也需要使用锁机制。某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，
# 其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，
# 从而保证了多线程情况下数据的正确性。

# 如果要确保balance计算正确，使用threading.Lock()来创建锁对象lock，把 lock.acquire()和lock.release()加在同步代码块里，
# 本例的同步代码块就是对全局变量balance进行先加后减操作

# 当某个线程执行change()函数时，通过lock.acquire()获取锁，那么其他线程就不能执行同步代码块了，只能等待知道锁被释放了，
# 获得锁才能执行同步代码块。由于锁只有一个，无论多少线程，同一个时刻最多只有一个线程持有该锁，所以修改全局变量balance不会产生冲突。
# 改良后的代码内容如下。

import threading

balance = 100
# 创建锁
lock = threading.Lock()


#def change(num, counter, lock):
def change(num, counter):
    global balance, lock
    for i in range(counter):
        # 加锁，只能有一个线程对balance操作
        if lock.acquire():
            balance = balance + num
            balance = balance - num
            # 释放锁
            lock.release()
        # 都是对balance操作，这两个锁，不管哪个线程拿到了，对balance的操作，只能有一个线程
        if lock.acquire():
            if balance != 100:
                # 如果输出这句话，说明线程不安全
                print("balance=%d" % balance)
                break
            lock.release()


if __name__ == "__main__":
    # thr1 = threading.Thread(target=change, args=(100, 500000, lock), name='t1')
    # thr2 = threading.Thread(target=change, args=(200, 500000, lock), name='t2')
    thr1 = threading.Thread(target=change, args=(100, 500000), name='t1')
    thr2 = threading.Thread(target=change, args=(200, 500000), name='t2')
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()
    print("{0} 线程结束".format(threading.current_thread().getName()))
