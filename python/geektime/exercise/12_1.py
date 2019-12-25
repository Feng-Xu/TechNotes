# 练习一 多线程文件名称查找
# 对某一文件夹启动10个线程查找文件包含abc三个字符的文件名，并显示该文件所在的路径
# 尽量使用面向对象编程方式实现

import os
import re
import threading
import time
import queue


# search('/Users/xufeng/Documents/workspace/python/geektime/', 'search')


# print(os.listdir('/Users/xufeng/Documents/workspace/python/geektime'))
# print(os.path.join('/Users/xufeng/Documents/workspace/python/geektime', 'classCode'))


class SearchAbc(threading.Thread):
    def __init__(self, queue, keyword):
        super().__init__()
        self.queue = queue
        self.keyword = keyword

    def search(self, keyword):
        while not self.queue.empty():
            filename = self.queue.get()
            # with open(file_path, 'rb') as f:
            with open(filename, encoding='utf-8') as f:
                context = f.read().replace("\n", " ")
                if len(re.findall(keyword, context)) != 0:
                    print(filename)
            self.queue.task_done()

    def run(self):
        # for _ in range(10):
        self.search(self.keyword)
        # print(threading.current_thread().getName(),threading.current_thread().ident)


# 存放目录中的文件名
filename_queue = queue.Queue()


# 将文件名放到队列中
def get_filename(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            filename_queue.put(file_path)
        elif os.path.isdir(file_path):
            get_filename(file_path)


get_filename('/Users/xufeng/Documents/workspace/python/geektime')
# while not filename_queue.empty():
#     print(filename_queue.get())

name_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_time = time.time()
# 存放线程
threads = []
for i in range(10):
    s = SearchAbc(filename_queue, 'search')
    s.setName(name_list[i])
    # 将两个线程任务加载到列表中
    threads.append(s)


# 运行线程，这个案例很常用，就是有多个函数要多线程执行的时候用到
for thread in threads:
    thread.start()
    # 线程堵塞 先运行第一个在运行第二个
    thread.join()


end_time = time.time()
print(end_time - start_time)
print('====end=====')
