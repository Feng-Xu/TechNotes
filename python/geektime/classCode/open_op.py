# # 将小说的人数记录在文件中
# # 写入
# file1 = open('name.txt','w', encoding='utf-8')
# file1.write('诸葛亮')
# file1.close()
#
# # 添加
# file2 = open('name.txt','a', encoding='utf-8')
# file2.write('\n刘备')
# file2.close()
#
# # 读取
# file3 = open('name.txt', encoding='utf-8')
# print(file3.read())

# 读取单行
# file4 = open('name.txt', encoding='utf-8')
# print(file4.readline())
# file4.close()

# 读取多行
# file5 = open('name.txt', encoding='utf-8')
# for line in file5.readlines():
#     print(line)
#     print('-----')
# file5.close()

# 当前文件指针   文件指针操作
file6  = open('name.txt', encoding='utf-8')
#print(file5.readlines())
print('当前文件的指针是 %s' % file6.tell())

print('读取一个字符，字符的内容是 %s' % file6.read(1))
print('当前文件的指针是 %s' % file6.tell())
# seek(4, 0)
#第一个参数表示偏移量，第二个参数  0 表示从文件开头便宜 1表示从当前位置便宜 2表示从文件结尾便宜
print('使用了seek（0）操作')
file6.seek(0)
print('当前文件的指针是 %s' % file6.tell())
file6.close()