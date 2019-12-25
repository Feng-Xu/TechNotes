# 1.创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和
def add():
    nums = input("请输入两个数次，用','分隔:")
    print(type(nums))
    # 当一些元素不用时，用_表示是更好的写法，可以让读代码的人知道这个元素是不要的
    # 多个元素不用时，则使用*_
    num1, *_, num2 = list(nums)
    print(type(num1))
    print(int(num1) + int(num2))

#add()


# 2. 创建一个函数，传入n个整数，返回其中最大的数和最小的数
# def find_num(list):
#     print('max:%d' % max(list))
#     print('min:%d' % min(list))
#
# list = [6, 2, 3, 4, 5]
# find_num(list)

def find_num(*args):
    print('max:%d' % max(list(args)))
    print('min:%d' % min(list(args)))

find_num(1,2,3,4,6,3,0)

# 3. 创建一个函数，传入一个参数n，返回n的阶乘

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

print(fact(7))


from functools import  reduce
num  = 7
# 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7
print(reduce(lambda x, y: x * y, range(1, num + 1)))