import time, signal


# 1. 统计函数开始执行和结束执行的时间
def time_out(second=10):
    def timmer(func):
        # 定义信号处理函数，改函数收到信号，进行处理
        def handler(signum, frame):
            raise TimeoutError('time out!')

        def wrapper(*args):
            # 对SIGALRM(终止)设置处理的handler，然后设置定时器，second后出发SIGALRM信号
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(second)
            try:
                start_time = time.time()
                print('start: %s' % start_time)
                func(*args)
                end_time = time.time()
                print('end: %s' % end_time)
                print('end - start: %s' % (end_time - start_time))
            finally:
                # 关闭定时器
                signal.alarm(0)

        return wrapper

    return timmer


@time_out(2)
def add(a, b):
    print(a + b)
    time.sleep(3)


try:
    add(3, 8)
except TimeoutError as e:
    print(e)
