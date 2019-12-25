# 练习三 列表的基本操作
# 定义一个含有5个数字的列表
# 为列表增加一个元素 100
# 使用remove()删除一个元素后观察列表的变化
# 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素

a_list = [1, 2, 3, 4, 5]
print(type(a_list))
a_list.append(100)
print(a_list)
a_list.remove(3)
print(a_list)
print(a_list[:3])
print(a_list[-1])