#
#
# @pysnooper.snoop()
# def yield_test(n):
#     for i in range(n):
#         yield call(i)
#         print("i=", i)
#         # 做一些其它的事情
#     print("do something.")
#     print("end.")
#
#
# def call(i):
#     return i * 2
#
#
# # 使用for循环
# # for i in yield_test(5):
# #     print(i, ",")
#
# print(type(yield_test(5)))
# a = yield_test(5)
# print(next(a))
# print("======")
# print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))


def func():
    x = 1
    while True:
        print(x)
        print("=======")
        y = (yield x)
        print(y)
        x += y

geniter = func()
geniter.__next__() # 1

geniter.send(3) # 4
geniter.send(10)# 14

# 输出结果：
# 1
# =======
# 3
# 4
# =======
# 10
# 14
# =======