import requests
import threading
import queue
import argparse

url = ""


class SystemInit(threading.Thread):
    def __init__(self, queue, version, service, monkey_token):
        super().__init__()
        self.queue = queue
        self.init_service = service
        self.version = version
        self.monkey_token = monkey_token

    def system_init(self):
        while not self.queue.empty():
            hostname = self.queue.get()
            data = {
                'hosts': [hostname, ],
                'os_version': self.version,
                'services': self.init_service,
                'executor': "Muti Scheduler",
            }

            headers = {"Content-Type": "application/json", 'Authorization': 'Token {}'.format(self.monkey_token)}

            req = requests.post(url, json=data, headers=headers)
            # 获取job_id
            job_id = req.json().get('job_id')
            # 获取执行结果
            req_result = requests.get('', params={'job_id': job_id})
            init_result = req_result.json().get('status')
            if init_result == 0:
                print(hostname.replace('\n', '') + " : 初始化成功")
            else:
                print(hostname.replace('\n', '') + " : ########初始化失败")
            self.queue.task_done()

    def run(self):
        self.system_init()
        # print(threading.current_thread().getName())


def get_monkey_token():
    data = {'username': '', 'password': ''}

    headers = {"Content-Type": "application/json"}

    req = requests.post('', json=data)
    if req.status_code == 200:
        return req.json().get('token')
    else:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="操作系统版本", type=int)
    parser.add_argument("-s", "--service", help="需要初始化的服务，使用‘,’隔开，为空则默认初始化java和flume", type=str)

    args = parser.parse_args()
    # 获取命令行参数
    os_verison = args.version
    init_service = args.service
    # 默认初始化java, flume, deploy
    init_service_list = ["java", "flume", "deploy"]

    if init_service is None:
        init_service_list_end = init_service_list
    else:
        # 获取用户输入的服务列表
        init_service_list_input = init_service.split(',')
        # 整合初始化服务并list去重
        init_service_list_end = list(set(init_service_list + init_service_list_input))

    # 主机名队列
    hosts_queue = queue.Queue()

    # 将主机名放入队列中
    with open('host_list.txt', encoding='utf-8') as hosts_file:
        for host in hosts_file.readlines():
            if host.replace('\n', '') != '':
                hosts_queue.put(host)

    # 获取monkey_token
    monkey_token = get_monkey_token()

    # 存放线程
    threads = []
    for i in range(4):
        s = SystemInit(hosts_queue, os_verison, init_service_list_end, monkey_token)
        # 将线程任务加载到列表中
        threads.append(s)

    # 运行线程，这个案例很常用，就是有多个函数要多线程执行的时候用到
    for thread in threads:
        thread.start()
        # 线程堵塞 先运行第一个在运行第二个
        thread.join()

    # 判断队列是否为空，然后清空host_list.txt文件
    if hosts_queue.empty():
        with open('host_list.txt', 'w', encoding='utf-8') as hosts_file:
            hosts_file.truncate()
            print("*********已清空host_list.txt，防止误操作*********")
