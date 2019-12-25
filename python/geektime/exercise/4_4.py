# 练习四 元组的基本操作
# 定义一个任意元组，对元组使用append() 查看错误信息
# 访问元组中的倒数第二个元素
# 定义一个新的元组，和 1. 的元组连接成一个新的元组
# 计算元组元素个数

tuple1 = ("string1", 1, (1,2))
print(tuple1)
# 对元组使用append() 查看错误信息
#tuple1.append(2)
print(tuple1[-2])
tuple2 = ('a', False, 2)
print(tuple2)

print(tuple1 + tuple2)

print(len(tuple1 + tuple2))
