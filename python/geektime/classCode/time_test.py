import time
print(time.time())
print(time.localtime())
# 格式化输出
print(time.strftime('%Y-%m-%d %H:%M:%S'))


import datetime
print(datetime.datetime.now())
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)

one_day = datetime.datetime(2018, 5, 27)
print(one_day)
new_time = datetime.timedelta(days=5)
print(one_day + new_time)
