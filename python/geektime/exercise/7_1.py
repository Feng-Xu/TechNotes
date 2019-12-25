# 练习一 文件的创建和使用
# # 创建一个文件，并写入当前日期
# # 再次打开这个文件，读取文件的前4个字符后退出
import time
cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
file_time = open('cur_time.txt','w')
file_time.write(cur_time)
file_time.close()

file_time1 = open('cur_time.txt')
file_time1.seek(0)
print('当前文件的指针是 %d' % file_time1.tell())
print('前四个字符是 %s' % file_time1.read(4))
file_time1.close()