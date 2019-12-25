import threading
import time
import random
import queue

queue1 = queue.Queue(2)

class ProducerThread(threading.Thread):
    def run(self):
        #global queue1
        nums = range(100)
        name = threading.current_thread().name
        while True:
            num = random.choice(nums)
            print("生产者 %s 生产 %s" % (name, num))
            queue1.put(num)
            t = random.randint(1, 3)
            time.sleep(t)
            print("生产者 %s 休眠了 %s 秒" % (name, t))

class ConsumerThread(threading.Thread):
    def run(self):
        #global queue1
        name = threading.current_thread().name
        while True:
            num = queue1.get()
            # 每task_done一次就从队列里删掉一个元素
            # 主要是给join用的，每次get后需要调用task_done，直到所有任务都task_done。join才取消阻塞
            # join()保持阻塞状态，直到处理了队列中的所有项目为止。在将一个项目添加到该队列时，未完成的任务的总数就会增加。
            # 当使用者线程调用 task_done() 以表示检索了该项目、并完成了所有的工作时，那么未完成的任务的总数就会减少。
            # 当未完成的任务的总数减少到零时，join() 就会结束阻塞状态。
            queue1.task_done()
            print("消费者 %s 消费 %s" % (name, num))
            t = random.randint(1,5)
            time.sleep(t)
            print("消费者 %s 休眠了 %s 秒" % (name, t))


p1 = ProducerThread(name='p1')
p2 = ProducerThread(name='p2')
p3 = ProducerThread(name='p3')
#c1 = ConsumerThread(name='c1')
p1.start()
p2.start()
p3.start()
#c1.start()
while True:
    time.sleep(1)
    print(queue1.qsize())